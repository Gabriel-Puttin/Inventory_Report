import xmltodict as xml
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        data = []
        file_type = path.split(".")[-1]
        if file_type == "xml":
            with open(path, encoding="utf-8") as file:
                products = xml.parse(file.read())
                data = products["dataset"]["record"]
        else:
            raise ValueError("Arquivo inválido")
        return data
