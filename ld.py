phones = ["ipone x", "xiaomi redmi3", "nokia 8080"]
products = [
    {"name": "Pillows 200*400 m", "stock": 25, "price": 80000, "description": "Очень красивая подушка", "recomend": phones},
    {"name": "Pillows 500 m", "stock": 50, "price": 90000, "description": "Очень красивая подушка2", "recomend": phones},
    {"name": "Pillows 1000 m", "stock": 100, "price": 100000, "description": "Очень красивая подушка3", "recomend": phones},
]
print(products[2]["recomend"][1])
