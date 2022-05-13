products_values = input().split()
products = {}
to_search = input().split()

for i in range(0, len(products_values), 2):
    key = products_values[i]
    quantity = products_values[i + 1]
    products[key] = int(quantity)

for product in to_search:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
