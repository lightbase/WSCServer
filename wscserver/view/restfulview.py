from pyramid_restler.view import RESTfulView
from collections import defaultdict
import json
import hashlib

class CustomRESTfulView(RESTfulView):

    """
    Classe com parametros personalizados de view dos registros
    para as classes WMI
    """

    def render_json(self, value):

        dados_banco = json.loads(self.context.to_json(value, self.fields,
                                 wrap=False))

        saida = {}
        results = []
        for computador in dados_banco:
            # Cria as chaves dos computadores
            saida[computador['id_computador']] = {}

        for computador in dados_banco:
            # Cria as chaves de classes nos computadores
            saida[computador['id_computador']][computador['nm_class_name']] = {}

        for x in dados_banco:
            # cria as chaves de propriedades nas classes
            saida[x['id_computador']][x['nm_class_name']][
                    x['nm_property_name']] = x['te_class_property_value']

        # Ordena os objetos json
        for computador in saida:
            classes = {}

            # Gera um hash para o id_computador
            salt = str('salthere').encode('utf-8')
            id_reg = str(computador).encode('utf-8')
            id_reg = hashlib.sha512(id_reg)
            id_reg.update(salt)
            id_reg = id_reg.hexdigest()
            classes['id_reg'] = id_reg

            for classe in saida[computador]:
                if classe != 'data_coleta':
                    # Aqui estou nas classes
                    classes[classe] = saida[computador][classe]

            results.append(classes)


        valores = {
            'results': results,
            'result_count': len(results)
        }

        response_data = dict(
            body=json.dumps(valores),
            content_type='application/json'
        )
        return response_data
