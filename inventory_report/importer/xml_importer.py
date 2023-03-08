import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, any_file):
        if any_file.endswith('xml'):
            with open(any_file, encoding="utf-8") as file:
                my_xml = file.read()
                my_list = xmltodict.parse(my_xml)
                products_list = my_list["dataset"]["record"]
                return products_list

        raise ValueError("Arquivo inválido")
