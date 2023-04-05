from inventory_report.inventory.product import Product

instruction = 'Local fechado à temperatura de 25°'


def test_relatorio_produto():
    'It class Product should print a correct string'
    product = Product(10, 'FireTV', 'Amazon', '04/04/2023', '04/04/2050',
                      500, instruction)
    assert product.id == 10
    assert product.nome_do_produto == 'FireTV'
    assert product.nome_da_empresa == 'Amazon'
    assert product.data_de_fabricacao == '04/04/2023'
    assert product.data_de_validade == '04/04/2050'
    assert product.numero_de_serie == 500
    assert product.instrucoes_de_armazenamento == instruction
