import json
import hashlib

from pyramid.response import Response
from wscserver.model import session


FILE_BEGIN = '{"results":['
FILE_END = '], "result_count": %s}'

# Computer class and properties filters
COMPUTER_FILTER = {
    "OperatingSystem": [
        "Caption",
        "Version",
        "InstallDate",
        # quantidade ???
    ],
    "Win32_Processor": [
        "Manufacturer",
        "Caption",
        "NumberOfLogicalProcessors",
        # idade ??
    ],
    "Win32_BIOS": [
        "Manufacturer",
    ],
    "SoftwareList": []
}

FILTER_KEYS = str(tuple(COMPUTER_FILTER.keys()))


def viewcoleta(request):

    #create index idx_id_computador on computador_coleta(id_computador);

    limit = request.params.get('limit', 'NULL')

    stmt1 = """
        SELECT 
            id_computador 
        FROM computador_coleta 
        GROUP BY id_computador
        LIMIT {};
    """.format(limit)

    computer_ids = session.execute(stmt1)


    stmt2 = """
        SELECT classe.nm_class_name,
               cp.nm_property_name,
               cc.te_class_property_value
        FROM computador_coleta AS cc
            INNER JOIN class_property as cp ON (cc.id_class_property =
                cp.id_class_property)
            INNER JOIN classe ON (classe.id_class = cp.id_class)
            WHERE cc.id_computador = {} AND
            classe.nm_class_name IN {};
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

    return Response('ok')
   #return Response(
   #    content_type='application/json',
   #    content_disposition='filename=coleta.json',
   #    app_iter=[open('/var/antony/coleta.json', 'rb').read()]
   #)



def build_computer_json(computer_group):

    computer = {
        "OperatingSystem": {},
        "Win32_Processor": {},
        "Win32_BIOS": {},
        "SoftwareList": []
    }

    for class_, property_, property_value in computer_group:

        if class_ == 'SoftwareList':
            if property_value.lower().find('office') > -1:
                computer[class_].append(property_value)
            elif property_value.lower().find('microsoft') > -1:
                computer[class_].append(property_value)
            continue

        elif property_ not in COMPUTER_FILTER[class_]:
            continue

        else:
            prefixed_property = class_ + '_' + property_
            computer[class_][prefixed_property] = property_value

    return json.dumps(computer)

def zipcoleta():
    """Recebe o json da coleta em um arquivo e zipa"""
    coleta = requests.get('http://localhost/wscserver/rest/coleta')

    tmpdir = tempfile.gettempdir()
    os.chdir(tmpdir)
    f = open('coleta.json','r')
    arquivozip = 'coleta.zip'
    with zipfile.ZipFile(arquivozip, 'w') as myzip:
        myzip.write(f.name)
    f.close()
    os.remove('coleta.json')
    filepath = os.path.abspath(arquivozip)
    return filepath
'''
def zipcoleta():
    """Recebe o json da coleta em um arquivo e zipa"""
    coleta = requests.get('http://localhost/wscserver/rest/coleta')

    path = tempfile.gettempdir()
    os.chdir(path)
    f = open('coleta.json','w')
    f.write(coleta.text)
    arquivozip = 'coleta.zip'
    with zipfile.ZipFile(arquivozip, 'w') as myzip:
        myzip.write(f.name)
    f.close()
    os.remove('coleta.json')
    filepath = os.path.abspath(arquivozip)
    return filepath
'''
