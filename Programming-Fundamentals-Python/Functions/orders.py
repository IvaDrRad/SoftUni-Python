def total_orders(product, number):
    if product == 'coffee':
        return number * 1.50
    elif product == 'water':
        return number
    if product == 'coke':
        return number * 1.40
    if product == 'snacks':
        return number * 2.00


current_product = input()
number_of_products = int(input())
print(f'{total_orders(current_product, number_of_products):.2f}')
