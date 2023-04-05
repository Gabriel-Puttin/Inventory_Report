from inventory_report.inventory.product import Product

instruction = "em local fechado à temperatura de 25°"
correct_string = (
    f"O produto FireTV fabricado em 04/04/2023 por Amazon com "
    f"validade até 04/04/2050 precisa ser armazenado {instruction}."
)


def test_cria_produto():
    "It class Product should return correct object"
    product = Product(
        10, "FireTV", "Amazon", "04/04/2023", "04/04/2050", 500, instruction
    )
    assert str(product) == correct_string
