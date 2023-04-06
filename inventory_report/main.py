import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def main():
    try:
        inventory = {}
        _, file, type_report = sys.argv
        path = sys.argv[1].split(".")[-1]

        if path == "csv":
            inventory = InventoryRefactor(CsvImporter)
        elif path == "json":
            inventory = InventoryRefactor(JsonImporter)
        else:
            inventory = InventoryRefactor(XmlImporter)

        inventory.import_data(file, type_report)
        reports = {
            "simples": SimpleReport.generate(inventory.data),
            "completo": CompleteReport.generate(inventory.data),
        }

        return sys.stdout.write(reports[type_report])

    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")
