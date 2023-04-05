from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(lista: list[dict]) -> str:
        simple_report = SimpleReport.generate(lista)
        companies = Counter([product["nome_da_empresa"] for product in lista])

        stocks = ""
        for company, amount in companies.items():
            stocks += f"- {company}: {amount}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{stocks}"
            )
