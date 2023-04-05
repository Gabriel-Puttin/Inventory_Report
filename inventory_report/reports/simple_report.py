from datetime import datetime
from collections import Counter


current_date = datetime.now()


class SimpleReport:
    @staticmethod
    def generate(lista: list[dict]) -> str:
        max_fab_date = max(
            lista,
            key=lambda sub: abs(
                datetime.strptime(sub["data_de_fabricacao"], "%Y-%m-%d")
                - current_date
            ),
        )["data_de_fabricacao"]

        min_valid_date = min(
            lista,
            key=lambda sub: abs(
                datetime.strptime(sub["data_de_validade"], "%Y-%m-%d")
                - current_date
            ),
        )["data_de_validade"]

        companies = Counter([product["nome_da_empresa"] for product in lista])
        most_repet_company = companies.most_common()[0][0]

        result = (
            f"Data de fabricação mais antiga: {max_fab_date}\n"
            f"Data de validade mais próxima: {min_valid_date}\n"
            f"Empresa com mais produtos: {most_repet_company}"
            )
        return result
