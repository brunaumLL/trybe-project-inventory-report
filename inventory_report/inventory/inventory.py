import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, any_file, type_report):
        if any_file.endswith('csv'):
            with open(any_file, encoding="utf-8") as file:
                [*products_list] = csv.DictReader(file)
        if any_file.endswith('.json'):
            with open(any_file, encoding="utf-8") as file:
                products_list = json.load(file)

        if type_report == "simples":
            return SimpleReport.generate(products_list)
        if type_report == "completo":
            return CompleteReport.generate(products_list)
