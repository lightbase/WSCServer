from pyramid_restler.view import RESTfulView
from collections import defaultdict
import json
import hashlib

class CustomRESTfulView(RESTfulView):

    """
    Classe com parametros personalizados de view dos registros
    para as classes WMI
    """

    def check_empty(self, classes, nome_classe):
        # Ensure variable is defined
        try:
            classe = classes[nome_classe]
        except KeyError:
            classe = {}
        return classe

    def render_json(self, value):

        dados_banco = json.loads(self.context.to_json(value, self.fields,
                                 wrap=False))

        saida = {}
        for computador in dados_banco:
            # Cria as chaves dos computadores
            saida[computador['id_computador']] = {}

        for x in dados_banco:
            # Cria as chaves de classes nos computadores
            saida[x['id_computador']][x['nm_class_name']] = {}

        for x in dados_banco:
            # cria as chaves de propriedades nas classes
            saida[x['id_computador']]['data_coleta'] = x['dt_hr_inclusao']
            saida[x['id_computador']][x['nm_class_name']][
                x['nm_property_name']] = x['te_class_property_value']

        results = []
        # Ordena os objetos json
        for computador in saida:
            # data_coleta = computador['dt_hr_inclusao'] <TODO>
            classes = {}
            for classe in saida[computador]:
                if classe != 'data_coleta':
                    # Aqui estou nas classes
                    classes[classe] = saida[computador][classe]

            # Gera um hash para o id_computador
            h = hashlib.sha256()
            h.update(str(computador).encode('utf-8'))
            computador = h.hexdigest()


            results.append({
                'id_reg': computador,
                'Win32_PhysicalMedia': [self.check_empty(classes, 'Win32_PhysicalMedia')],
                'Win32_ComputerSystem': [self.check_empty(classes, 'Win32_ComputerSystem')],
                'Win32_Keyboard': [self.check_empty(classes, 'Win32_Keyboard')],
                'Win32_NetworkAdapter': [self.check_empty(classes, 'Win32_NetworkAdapter')],
                'Win32_PointingDevice': [self.check_empty(classes, 'Win32_PointingDevice')],
                'Win32_MemoryDevice': [self.check_empty(classes, 'Win32_MemoryDevice')],
                'Win32_PhysicalMemory': [self.check_empty(classes, 'Win32_PhysicalMemory')],
                'Win32_BaseBoard': [self.check_empty(classes, 'Win32_BaseBoard')],
                'Win32_Printer': [self.check_empty(classes, 'Win32_Printer')],
                'Win32_Processor': [self.check_empty(classes, 'Win32_Processor')],
                'Win32_DesktopMonitor': [self.check_empty(classes, 'Win32_DesktopMonitor')],
                'Win32_BIOS': [self.check_empty(classes, 'Win32_BIOS')],
            })

        valores = {
            'results': results,
            'result_count': len(results)
        }

        response_data = dict(
            body=json.dumps(valores),
            content_type='application/json'
        )
        return response_data
