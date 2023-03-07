from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        'Lápis Bonito',
        'Empresa Bonita',
        '2023-01-01',
        '2024-01-01',
        'A0B1',
        'Guarde com carinho'
    )
    result = product.__repr__()
    assert result == (
            f"O produto {product.nome_do_produto}"
            f" fabricado em {product.data_de_fabricacao}"
            f" por {product.nome_da_empresa} com validade"
            f" até {product.data_de_validade}"
            f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
        )
