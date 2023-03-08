from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    products = [
        {
            "id": 1,
            "nome_do_produto": "Lápis Bonito",
            "nome_da_empresa": "Empresa Bonita",
            "data_de_fabricacao": "2023-01-01",
            "data_de_validade": "2024-01-01",
            "numero_de_serie": "A0B1",
            "instrucoes_de_armazenamento": "Guarde com carinho",
        }
    ]

    GREEN = "\033[32m"
    BLUE = "\033[36m"
    RED = "\033[31m"
    END = "\033[0m"

    expected_result = (
        f"{GREEN}Data de fabricação mais antiga:{END} {BLUE}2023-01-01{END}\n"
        f"{GREEN}Data de validade mais próxima:{END} {BLUE}2024-01-01{END}\n"
        f"{GREEN}Empresa com mais produtos:{END} {RED}Empresa Bonita{END}"
    )

    result_colored_simple = ColoredReport(SimpleReport).generate(products)
    result_colored_complete = ColoredReport(CompleteReport).generate(products)

    assert expected_result in result_colored_simple
    assert expected_result in result_colored_complete
