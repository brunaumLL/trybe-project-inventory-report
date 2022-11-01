import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(a, any_file):
        if any_file.endswith("json"):
            with open(any_file) as file:
                products_list = json.load(file)
                return products_list

        raise ValueError("Arquivo inválido")
