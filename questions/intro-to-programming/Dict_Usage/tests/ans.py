

products_number = list(products.keys())

product_info = products[data["params"]["prod_info"]]

product_name = ""
for num in products_number:
    if products[num]["price"] == float(data["params"]["price"]):
        product_name = products[num]["name"]
        break