command = input()
products = {}
while command != 'statistics':
    command = command.split(': ')
    product, quantity = command
    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)
    command = input()

print('Products in stock:')
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
