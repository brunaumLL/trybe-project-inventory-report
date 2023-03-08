import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, any_file):
        if any_file.endswith('csv'):
            with open(any_file, encoding="utf-8") as file:
                [*products_list] = csv.DictReader(file)
                return products_list

        raise ValueError("Arquivo inválido")
