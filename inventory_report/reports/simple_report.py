from statistics import mode


class SimpleReport:
    @classmethod
    def generate(cls, list):
        earliest_date = min(product['data_de_fabricacao'] for product in list)
        latest_date = min(product['data_de_validade'] for product in list)
        more_products = mode(product['nome_da_empresa'] for product in list)

        return (
            f"Data de fabricação mais antiga: {earliest_date}\n"
            f"Data de validade mais próxima: {latest_date}\n"
            f"Empresa com mais produtos: {more_products}"
        )
