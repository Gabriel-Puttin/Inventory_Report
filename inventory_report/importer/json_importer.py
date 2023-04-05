import pandas as pd
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        data = []
        file_type = path.split(".")[-1]
        if file_type == "json":
            data = pd.read_json(path, dtype={"id": str}).to_dict("records")
        else:
            raise ValueError("Arquivo inválido")
        return data
