from menu import products


def get_product_by_id(id: int) -> dict[str, any]:
    if not (type(id) is int):
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product

    return {}


def get_products_by_type(by_type: str) -> list[dict[str, any]]:
    if not (type(by_type) is str):
        raise TypeError("product type must be a str")
    return [product for product in products if product["type"] == by_type]


def add_product(menu: list[dict[str, any]] | list, **new_product: dict) -> dict[str, any]:
    id: int = 0
    for product in menu:
        if product["_id"] > id:
            id = product["_id"]
    id = id + 1

    new_product["_id"] = id

    menu.append(new_product)
    return new_product


def menu_report():
    contagem_de_produtos: int = len(products)
    preco_medio: float = 0
    for i in products:
        preco_medio = preco_medio + i["price"]

    preco_medio = preco_medio / contagem_de_produtos
    preco_medio = round(preco_medio, 2)

    tipos: list = []
    for product in products:
        if not tipos:
            tipos.append(product["type"])
            break
        for item in tipos:
            if not item == product["type"]:
                tipos.add(product["type"])

    tipo_mais_comum: str = ""
    comeco: int = 0
    contagem: int = 0

    for tipo in tipos:
        for i in range(len(products)):
            if tipo == products[i]["type"]:
                contagem = contagem + 1
        if contagem > comeco:
            contagem = comeco
            tipo_mais_comum = tipo
            comeco = 0

    return f"Products Count: {contagem_de_produtos} - Average Price: ${preco_medio} - Most Common Type: {tipo_mais_comum}"
