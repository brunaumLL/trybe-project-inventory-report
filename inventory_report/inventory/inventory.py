import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(a, file_csv, report_type):
        with open(file_csv, encoding="utf-8") as file:
            [*products_list] = csv.DictReader(file)

        if report_type == "simples":
            return SimpleReport.generate(products_list)
        if report_type == "completo":
            return CompleteReport.generate(products_list)
