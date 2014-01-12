import zipfile
import tempfile
import requests
import os

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
