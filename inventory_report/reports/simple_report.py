from statistics import mode


class SimpleReport:
    @classmethod
    def generate(a, list):
        oldest_date = min([product["data_de_fabricacao"] for product in list])
        closest_date = min([product["data_de_validade"] for product in list])
        company_bigger_stock = mode(
            [product["nome_da_empresa"] for product in list])
        return(
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
