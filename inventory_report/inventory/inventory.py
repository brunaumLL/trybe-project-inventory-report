import csv
import json
import xmltodict
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, any_file, type_report):
        if any_file.endswith('csv'):
            with open(any_file, encoding="utf-8") as file:
                [*products_list] = csv.DictReader(file)
        elif any_file.endswith('.json'):
            with open(any_file, encoding="utf-8") as file:
                products_list = json.load(file)
        else:
            with open(any_file, encoding="utf-8") as file:
                my_xml = file.read()
                my_list = xmltodict.parse(my_xml)
                products_list = my_list["dataset"]["record"]

        if type_report == "simples":
            return SimpleReport.generate(products_list)
        if type_report == "completo":
            return CompleteReport.generate(products_list)
