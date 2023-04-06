from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer: list[dict]) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, file: str, type: str):
        self.data = [*self.data, *self.importer.import_data(file)]

        reports = {
            "simples": SimpleReport.generate(self.data),
            "completo": CompleteReport.generate(self.data),
        }

        return reports[type]

    def __iter__(self):
        return InventoryIterator(self.data)
