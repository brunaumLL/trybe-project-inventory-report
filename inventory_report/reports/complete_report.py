from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        company_stock = dict(
            Counter(product['nome_da_empresa'] for product in list))

        company_stock_quantity = ''

        for company in company_stock:
            company_stock_quantity += (
                f"- {company}: {company_stock[company]}\n"
            )

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{company_stock_quantity}"
        )
