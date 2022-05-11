def collect_material(products_dict: dict, junk_materials: dict, material: str, quantity: int):
    if material == "shards" or material == "fragments" or material == "motes":
        products_dict[material] += quantity
    else:
        if material not in junk_materials:
            junk_materials[material] = quantity
        else:
            junk_materials[material] += quantity


products = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_obtained = ''
# item_list = []
# quantity_list = []
while item_obtained == '':
    items = input().split()
    for index in range(0, len(items), 2):
            quantity = int(items[index])
            material = str(items[index + 1]).lower()

            collect_material(products, junk, material, quantity)

            if products["shards"] >= 250:
                item_obtained = "Shadowmourne"
                products["shards"] -= 250
                break
            elif products["fragments"] >= 250:
                item_obtained = "Valanyr"
                products["fragments"] -= 250
                break
            elif products["motes"] >= 250:
                item_obtained = "Dragonwrath"
                products["motes"] -= 250
                break

print(f"{item_obtained} obtained!")

for key, value in products.items():
    print(f"{key}: {value}")

for key, value in junk.items():
    print(f"{key}: {value}")




