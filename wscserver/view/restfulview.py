import json
from pyramid.response import Response
from wscserver.model import session
import zipfile
import re
from logging import getLogger

FILE_BEGIN = '{"results":['
FILE_END = '], "result_count": %s}'

# Computer class and properties filters
COMPUTER_FILTER = {
    "OperatingSystem": [
        "Caption",
        "Version",
        "InstallDate"
    ],
    "Win32_Processor": [
        "Manufacturer",
        "Caption",
        "NumberOfLogicalProcessors",
        "MaxClockSpeed",
        "Family"
    ],
    "Win32_BIOS": [
        "Manufacturer",
    ],
    "Win32_PhysicalMemory": [
        "MemoryType",
        "Capacity"
    ],
    "Win32_LogicalDisk": [
        "Caption",
        "MediaType",
        "Size"
    ],
    "SoftwareList": []
}

FILTER_KEYS = str(tuple(COMPUTER_FILTER.keys()))

log = getLogger()


def viewcoleta(request):

    # Please ensure this index exists on database
    # CREATE INDEX idx_id_computador ON computador_coleta(id_computador);
    if request.params.get('limit') is None:
        stmt1 = """
        SELECT id_computador
        FROM computador_coleta
        GROUP BY id_computador;
        """
    else:
        stmt1 = """
            SELECT id_computador
            FROM computador_coleta
            GROUP BY id_computador
            LIMIT {};
            """.format(request.params.get('limit'))

    computer_ids = session.execute(stmt1)

    stmt2 = """
        SELECT classe.nm_class_name,
               cp.nm_property_name,
               cc.te_class_property_value,
               pr.display_name
        FROM computador_coleta AS cc
            INNER JOIN class_property as cp ON (cc.id_class_property =
                cp.id_class_property)
            INNER JOIN classe ON (classe.id_class = cp.id_class)
            LEFT JOIN proriedade_software pr ON (
              cp.id_class_property = pr.id_class_property
              AND cc.id_computador = pr.id_computador
              AND lower(pr.display_name) LIKE lower('%office%'))
        WHERE cc.id_computador = {}
        AND classe.nm_class_name IN {};
        """

    with open('/tmp/coleta.json', 'w') as f:

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

        with zipfile.ZipFile('/tmp/coleta.zip', 'w') as myzip:
            myzip.write('/tmp/coleta.json')

        return Response(
           content_type='application/zip',
           content_disposition='filename=coleta.zip',
           body_file=open('/tmp/coleta.zip', 'rb'))
    else:
        return Response(
           content_type='application/json',
           content_disposition='filename=coleta.json',
           body_file=open('/tmp/coleta.json'))

    return Response('ok')


def build_computer_json(computer_group):

    computer = {
        "OperatingSystem".lower(): {},
        "Win32_Processor".lower(): {},
        "Win32_BIOS".lower(): {},
        "Win32_PhysicalMemory".lower(): {},
        "Win32_LogicalDisk".lower(): {},
        "SoftwareList".lower(): []
    }

    # FIXME: Arrumar uma forma melhor de definir os atributos que devem ser somados
    somar = [
        "NumberOfLogicalProcessors",
        "Capacity"
    ]

    for class_, property_, property_value, display_name in computer_group:

        if class_ == 'SoftwareList'.lower():
            if display_name is not None:
                computer[class_.lower()].append(display_name)
            #elif property_.lower().find('microsoft') > -1:
            #    computer[class_].append(property_)
            continue

        elif property_ not in COMPUTER_FILTER[class_]:
            continue

        else:
            prefixed_property = class_ + '_' + property_

            # Fix no valor da propriedade quando mutivalorado
            p = property_value.split("[[REG]]")
            if type(p) == list and len(p) > 0:
                saida = int()
                for value in p:
                    if value.isdigit():
                        if property_ in somar:
                            log.debug(value)
                            saida += int(value)
                        else:
                            saida = int(value)
                    else:
                        saida = value
                property_value = saida

            computer[class_.lower()][prefixed_property.lower()] = property_value

    return json.dumps(computer)

