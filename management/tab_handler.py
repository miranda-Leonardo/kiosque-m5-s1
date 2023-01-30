from menu import products


def calculate_tab(table_orders: list[dict[str, int]]) -> dict[str, str]:
    subtotal = 0
    for table_order in table_orders:
        for product in products:
            if table_order["_id"] == product["_id"]:
                subtotal = subtotal + product["price"] * table_order["amount"]
                break
    return dict({"subtotal": f"${str(round(subtotal, 2))}"})
