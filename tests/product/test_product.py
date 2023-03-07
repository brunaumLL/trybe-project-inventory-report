from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Lápis Bonito',
        'Empresa Bonita',
        '2023-01-01',
        '2024-01-01',
        'A0B1',
        'Guarde com carinho'
    )
    assert product.id == int(1)
    assert product.nome_do_produto == str('Lápis Bonito')
    assert product.nome_da_empresa == str('Empresa Bonita')
    assert product.data_de_fabricacao == str('2023-01-01')
    assert product.data_de_validade == str('2024-01-01')
    assert product.numero_de_serie == str('A0B1')
    assert product.instrucoes_de_armazenamento == str('Guarde com carinho')
