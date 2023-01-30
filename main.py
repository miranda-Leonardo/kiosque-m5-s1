from management.product_handler import get_product_by_id, get_products_by_type, add_product, menu_report
from management.tab_handler import calculate_tab

if __name__ == "__main__":
    # Seus prints de teste aqui
    # print(get_product_by_id(28))
    # print(get_product_by_id('b'))
    # print(get_products_by_type("drink"))
    # print(get_products_by_type(1))
    # my_list = []
    # new_product = {
    #     "title": "X-Python",
    #     "price": 5.0,
    #     "rating": 5,
    #     "description": "Sanduiche de Python",
    #     "type": "fast-food",
    # }
    # print(add_product(my_list, **new_product))
    # print(my_list)
    # table_orders1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    # table_orders2 = [
    #     {"_id": 10, "amount": 3},
    #     {"_id": 20, "amount": 2},
    #     {"_id": 21, "amount": 5},
    # ]
    # print(calculate_tab(table_orders1))
    # print(calculate_tab(table_orders2))
    print(menu_report())
    ...
