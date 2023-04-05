import pandas as pd
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        data = []
        file_type = path.split(".")[-1]
        if file_type == "csv":
            data = pd.read_csv(path, converters={"id": str}).to_dict("records")
        else:
            raise ValueError("Arquivo inválido")
        return data
