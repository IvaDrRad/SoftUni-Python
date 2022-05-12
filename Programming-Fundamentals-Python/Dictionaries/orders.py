# import collections

def add_product(quantity_dict: dict, price_dict: dict, pr_name: str, pr_price: float, pr_qty: int):
    if pr_name not in quantity_dict:
        quantity_dict[pr_name] = pr_qty
    else:
        quantity_dict[pr_name] += pr_qty
    price_dict[pr_name] = pr_price


dict_merged = {}    #collections.defaultdict(float)
products_quantity_dict = {}
products_price_dict = {}
command = input()
while command != "buy":
    command = command.split()
    name = command[0]
    price = float(command[1])
    quantity = int(command[2])
    add_product(products_quantity_dict, products_price_dict, name, price, quantity)

    command = input()

for key, v1 in products_quantity_dict.items():
        dict_merged[key] = v1 * products_price_dict[key]


for key, value in dict_merged.items():
    print(f"{key} -> {value:.2f}")
