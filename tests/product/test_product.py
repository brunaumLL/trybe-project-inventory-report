from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Borracha",
        "Papelaria Solar",
        "2021-07-04",
        "2029-02-09",
        "FR48",
        "Ao abrigo de luz solar")
    assert product.id == int(1)
    assert product.nome_do_produto == str("Borracha")
    assert product.nome_da_empresa == str("Papelaria Solar")
    assert product.data_de_fabricacao == str("2021-07-04")
    assert product.data_de_validade == str("2029-02-09")
    assert product.numero_de_serie == str("FR48")
    assert product.instrucoes_de_armazenamento == str("Ao abrigo de luz solar")
