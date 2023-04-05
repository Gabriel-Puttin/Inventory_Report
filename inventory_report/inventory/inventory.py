import pandas as pd
import xmltodict as xml
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type_report: str):
        data = {}
        file_type = path.split('.')[-1]
        if (file_type == 'csv'):
            data = pd.read_csv(path).to_dict('records')
        elif (file_type == 'json'):
            data = pd.read_json(path).to_dict('records')
        else:
            with open(path, encoding="utf-8") as file:
                products = xml.parse(file.read())
                data = products["dataset"]["record"]

        reports = {
            "simples": SimpleReport.generate(data),
            "completo": CompleteReport.generate(data),
        }

        return reports[type_report]
