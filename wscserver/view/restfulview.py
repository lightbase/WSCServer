from pyramid_restler.view import RESTfulView
from collections import defaultdict
import json
import hashlib
from itertools import groupby

class CustomRESTfulView(RESTfulView):

    """
    Classe com parametros personalizados de view dos registros
    para as classes WMI
    """

    # Computer class and properties filters
    computer_filter = {
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
    }

    def render_json(self, collection):

        """
        :param collection: List of <wscserver.model.Coleta.Coleta object>
        collection element attributes example:

        "id_class": 3,
        "id_computador_coleta_historico": 1,
        "nm_class_name": "NetworkAdapterConfiguration",
        "nm_property_name": "Description",
        "id_computador_coleta": 1,
        "id_class_property": 6,
        "dt_hr_inclusao": "2014-07-18 12:34:43",
        "id_computador": 3,
        "te_class_property_value": " "Intel(R) 82579V Gigabit Network Connection"
        """

        def keyfunc(obj):
            # Will group by computer ID
            return int(obj.id_computador)

        # Sort list before grouping
        collection = sorted(collection, key=keyfunc)

        # Create result list
        computers = [ ]

        # Navigate groups
        for id_computador, computer_group in groupby(collection, keyfunc):

            computer = { }

            for collection_element in list(computer_group):

                class_ = collection_element.nm_class_name
                property_ = collection_element.nm_property_name
                property_value = collection_element.te_class_property_value

                if class_ not in self.computer_filter:
                    # Filter classes
                    continue

                if property_ not in self.computer_filter[class_]:
                    # Filter properties 
                    continue

                if computer.get(class_) is None:
                    computer[class_] = { }
                else:
                    prefixed_property = class_ + '_' + property_
                    computer[class_][prefixed_property] = property_value

            computers.append(computer)

        response = {
            'results': computers,
            'result_count': len(computers)
        }

        return dict(
            body=json.dumps(response),
            content_type='application/json'
        )


