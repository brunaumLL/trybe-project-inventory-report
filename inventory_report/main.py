import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    if sys.argv[1].endswith("csv"):
        importer = CsvImporter
    if sys.argv[1].endswith("json"):
        importer = JsonImporter
    if sys.argv[1].endswith("xml"):
        importer = XmlImporter

    inventories = InventoryRefactor(importer)
    sys.stdout.write(inventories.import_data(sys.argv[1], sys.argv[2]))
