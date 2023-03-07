import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, file_csv, type_report):
        if file_csv.endswith('csv'):
            with open(file_csv, encoding="utf-8") as file:
                [*products_list] = csv.DictReader(file)

        if type_report == "simples":
            return SimpleReport.generate(products_list)
        if type_report == "completo":
            return CompleteReport.generate(products_list)
