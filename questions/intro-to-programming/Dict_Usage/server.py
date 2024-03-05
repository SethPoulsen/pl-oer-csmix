
def generate(data):

    names_for_user = [ 
        {"name": "products", "type": "dictionary", "description": "a dict containing all the product information"},
    ]
    names_from_user = [ 
        {"name": "products_number", "type": "list", "description": "a list containing all the product numbers"},
        {"name": "product_info", "type": "dictionary", "description": "the product info given the product number"},
        {"name": "product_name", "type": "string", "description": "the product name given the product price"},
    ]
    
    
    product_info = {
        'P100': {'name': 'Travel Mug', 'price': 12.99},
        'P200': {'name': 'Tea Kettle', 'price': 25.99},
        'P300': {'name': 'Desk Lamp', 'price': 45.50},
        'P400': {'name': 'Notebook', 'price': 3.99},
        'P500': {'name': 'Water Bottle', 'price': 20.00},
        'P600': {'name': 'Wall Clock', 'price': 30.25},
        'P700': {'name': 'Tablecloth', 'price': 17.75},
        'P800': {'name': 'Scented Candle', 'price': 8.99},
        'P900': {'name': 'Plant Pot', 'price': 5.55},
        'P1000': {'name': 'Flash Drive', 'price': 12.95},
        'P1100': {'name': 'Wireless Mouse', 'price': 29.99},
        'P1200': {'name': 'Keyboard', 'price': 55.00},
        'P1300': {'name': 'Earbuds', 'price': 19.99},
        'P1400': {'name': 'Smartphone Stand', 'price': 9.99},
        'P1500': {'name': 'Desk Organizer', 'price': 16.99},
        'P1600': {'name': 'Backpack', 'price': 49.99},
        'P1700': {'name': 'Lunch Box', 'price': 14.99},
        'P1800': {'name': 'Hand Sanitizer', 'price': 2.99},
        'P1900': {'name': 'Calculator', 'price': 11.99},
        'P2000': {'name': 'HDMI Cable', 'price': 6.99}
    }
    
    import random
    data["params"]['prod_info'] = random.choice(list(product_info.keys()))
    data["params"]['price'] = "{:,.2f}".format(product_info[random.choice(list(product_info.keys()))]['price'])
    data["params"]["names_for_user"] = names_for_user
    data["params"]["names_from_user"] = names_from_user
    
    return data