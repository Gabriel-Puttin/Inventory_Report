from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(path: str, type_report: str):
        data = []
        file_type = path.split('.')[-1]
        if (file_type == 'csv'):
            data = CsvImporter.import_data(path)
        elif (file_type == 'json'):
            data = JsonImporter.import_data(path)
        else:
            data = XmlImporter.import_data(path)

        reports = {
            "simples": SimpleReport.generate(data),
            "completo": CompleteReport.generate(data),
        }

        return reports[type_report]
