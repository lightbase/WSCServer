#!/usr/env python
# -*- coding: utf-8 -*-
import logging
import json
from pyramid.response import Response
from ..model import session, tmp_dir, extended
import zipfile
import uuid
import hashlib

log = logging.getLogger()

FILE_BEGIN = '{"results":['
FILE_END = '], "result_count": %s}'

# Computer class and properties filters
COMPUTER_FILTER = {
    "OperatingSystem": [
        "Caption".lower(),
        "Version".lower(),
        "InstallDate".lower()
    ],
    "Win32_Processor": [
        "Manufacturer".lower(),
        "Caption".lower(),
        "NumberOfLogicalProcessors".lower(),
        "MaxClockSpeed".lower(),
        "Family".lower()
    ],
    "Win32_BIOS": [
        "Manufacturer".lower(),
    ],
    "Win32_PhysicalMemory": [
        "MemoryType".lower(),
        "Capacity".lower()
    ],
    "Win32_DiskDrive": [
        "Caption".lower(),
        "Model".lower(),
        "Size".lower()
    ],
    "SoftwareList": []
}


# Adição Jansen: 2015-1126
# Adiciona atributos da coleta estendida
if extended:
    COMPUTER_FILTER['Win32_BaseBoard'] = ["InstallDate".lower()]
    COMPUTER_FILTER['Win32_BIOS'].append("InstallDate".lower())
    COMPUTER_FILTER['Win32_BIOS'].append("ReleaseDate".lower())
    COMPUTER_FILTER['Win32_Processor'].append("InstallDate".lower())

log.debug(COMPUTER_FILTER)

FILTER_KEYS = str(tuple(COMPUTER_FILTER.keys()))

def viewcoleta(request):
    filename = tmp_dir + '/coleta-' + str(uuid.uuid4())
    json_file = filename + '.json'
    zip_file = filename + '.zip'
    # Please ensure this index exists on database
    # CREATE INDEX idx_id_computador ON computador_coleta(id_computador);
    if request.params.get('limit') is None:
        stmt1 = """
        SELECT DISTINCT cl.id_computador
        FROM computador_coleta cl
        INNER JOIN computador c ON cl.id_computador = c.id_computador
        WHERE (c.ativo IS NULL or c.ativo = 't')
        ORDER BY cl.id_computador DESC;
        """
    else:
        stmt1 = """
            SELECT DISTINCT cl.id_computador
            FROM computador_coleta cl
            INNER JOIN computador c ON cl.id_computador = c.id_computador
            WHERE (c.ativo IS NULL or c.ativo = 't')
            ORDER BY cl.id_computador DESC
            LIMIT {};
            """.format(request.params.get('limit'))

    computer_ids = session.execute(stmt1)

    stmt2 = """
        SELECT cc.id_computador,
               classe.nm_class_name,
               cp.nm_property_name,
               cc.te_class_property_value,
               pr.display_name,
               cc.dt_hr_inclusao as data_coleta,
               c.dt_hr_ult_acesso as data_ultimo_acesso,
               c.te_node_address as mac,
               c.te_ip_computador as ip_computador,
               r.te_ip_rede as ip_rede,
               r.nm_rede as nome_rede
        FROM computador_coleta AS cc
            INNER JOIN computador c ON cc.id_computador = c.id_computador
            INNER JOIN rede r ON c.id_rede = r.id_rede
            INNER JOIN class_property as cp ON (cc.id_class_property =
                cp.id_class_property)
            INNER JOIN classe ON (classe.id_class = cp.id_class)
            LEFT JOIN proriedade_software pr ON (
              cp.id_class_property = pr.id_class_property
              AND cc.id_computador = pr.id_computador)
        WHERE cc.id_computador = {}
        AND classe.nm_class_name IN {};
        """

    with open(json_file, 'w') as f:

        f.write(FILE_BEGIN)

        count = computer_ids.rowcount

        for (id_computador, ) in computer_ids.fetchall():

            computer_attributes = session.execute(
                stmt2.format(id_computador, FILTER_KEYS)).fetchall()
            computer_json = build_computer_json(computer_attributes)

            f.write(computer_json)
            count -= 1

            if count is not 0:
                f.write(',')

        f.write(FILE_END % computer_ids.rowcount)

    if '1' in tuple(request.params.get('zip', '0')):

        with zipfile.ZipFile(zip_file, 'w') as myzip:
            myzip.write(json_file)

        return Response(
            content_type='application/zip',
            content_disposition='filename=coleta.zip',
            body_file=open(zip_file, 'rb')
        )
    else:
        return Response(
            content_type='application/json',
            content_disposition='filename=coleta.json',
            body_file=open(json_file, 'rb')
        )


def build_computer_json(computer_group):

    computer = {
        "OperatingSystem".lower(): {},
        "Win32_Processor".lower(): {},
        "Win32_BIOS".lower(): {},
        "Win32_PhysicalMemory".lower(): {},
        "Win32_DiskDrive".lower(): {},
        "SoftwareList".lower(): []
    }

    # Jansen: 2015-11-26
    # Adiciona atributos extras
    if extended:
        computer['Win32_BaseBoard'.lower()] = {}

    # FIXME: Arrumar uma forma melhor de definir os atributos que devem ser somados
    somar = [
        "NumberOfLogicalProcessors".lower(),
        "Capacity".lower(),
        "Size".lower()
    ]

    for id_computador, class_, property_, property_value, display_name, data_coleta, \
        data_ultimo_acesso, mac, ip_computador, ip_rede, nome_rede in computer_group:

        # Gera um hash para o id_computador
        salt = str('salthere').encode('utf-8')
        id_reg = str(id_computador).encode('utf-8')
        id_reg = hashlib.sha512(id_reg)
        id_reg.update(salt)
        id_reg = id_reg.hexdigest()

        # Adiciona um hash para cada computador
        computer['hash_machine'] = id_reg

        # Data da coleta
        computer['data_coleta'] = data_coleta.strftime("%d/%m/%Y %H:%M:%S")
        computer['data_ultimo_acesso'] = data_ultimo_acesso.strftime("%d/%m/%Y %H:%M:%S")

        # Jansen: 2015-11-26
        # Adiciona atributos extras
        if extended:
            computer['mac'] = mac
            computer['ip_computador'] = ip_computador
            computer['ip_rede'] = ip_rede
            computer['nome_rede'] = nome_rede

        if class_ == 'SoftwareList':
            if display_name is not None and \
                    display_name.lower().find('office') > -1:
                computer[class_.lower()].append(display_name)
            #elif property_.lower().find('microsoft') > -1:
            #    computer[class_].append(property_)
            continue

        elif property_.lower() not in COMPUTER_FILTER[class_]:
            continue

        else:
            prefixed_property = class_ + '_' + property_

            # Fix no valor da propriedade quando mutivalorado
            p = property_value.split("[[REG]]")
            if type(p) == list and len(p) > 0:
                saida = int()
                for value in p:
                    # Corrige erro do campo bytes
                    value = value.strip("bytes").strip()
                    value = value.strip("Hz").strip()
                    if value.isdigit():
                        if property_.lower() in somar:
                            log.debug(value)
                            saida += int(value)
                        else:
                            saida = int(value)
                    else:
                        saida = value
                property_value = saida

            computer[class_.lower()][prefixed_property.lower()] = property_value

    return json.dumps(computer)

