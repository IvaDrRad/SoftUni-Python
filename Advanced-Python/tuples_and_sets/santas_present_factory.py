from collections import deque

materials = [int(el) for el in input().split()]
values = deque([int(el) for el in input().split()])
magic_needed = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
toys = {}

while materials and magic_needed and values:
    material = materials.pop()
    value = values.popleft()
    total_magic = material * value

    if material == 0 and value == 0:
        continue
    if material == 0:
        values.appendleft(value)
    if value == 0:
        materials.append(material)

    if total_magic in magic_needed:
        toy_name = magic_needed[total_magic]

        if toy_name not in toys:
            toys[toy_name] = 1
        else:
            toys[toy_name] += 1
        continue

    if total_magic < 0:
        sums = material + value
        materials.append(sums)
    elif total_magic > 0:
        materials.append(material + 15)


if 'Doll' in toys and 'Wooden train' in toys or 'Teddy bear' in toys and 'Bicycle' in toys:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    materials_as_str = [str(m) for m in materials]
    materials_as_str.reverse()
    print(f"Materials left: {', '.join(materials_as_str)}")
if values:
    values_as_str = [str(v) for v in values]
    print(f"Magic left: {', '.join(values_as_str)}")
for toy, amount in sorted(toys.items()):
    print(f"{toy}: {amount}")

# # 80/100 !
# from collections import deque
#
# materials = [int(el) for el in input().split()]
# values = deque([int(el) for el in input().split()])
# magic_needed = {150, 250, 300, 400}
# toys = {}
# there_are_presents = False
#
# while materials and magic_needed and values:
#     total_magic = materials[-1] * values[0]
#     if total_magic in magic_needed:
#         materials.pop()
#         values.popleft()
#         if total_magic == 150:
#             if 'Doll' not in toys:
#                 toys['Doll'] = 0
#             toys['Doll'] += 1
#         elif total_magic == 250:
#             if 'Wooden train' not in toys:
#                 toys['Wooden train'] += 1
#             toys['Wooden train'] += 1
#         elif total_magic == 300:
#             if 'Teddy bear' not in toys:
#                 toys['Teddy bear'] = 0
#             toys['Teddy bear'] += 1
#         elif total_magic == 400:
#             if 'Bicycle' not in toys:
#                 toys['Bicycle'] = 0
#             toys['Bicycle'] += 1
#         if 'Doll' in toys and 'Wooden train' in toys or 'Teddy bear' in toys and 'Bicycle' in toys:
#           there_are_presents = True
#     else:
#         if total_magic < 0:
#             sums = materials[-1] + values[0]
#             materials.pop()
#             values.popleft()
#             materials.append(sums)
#         elif total_magic > 0:
#             values.popleft()
#             materials[-1] += 15
#         else:
#             if materials[-1] == 0 and values[0] == 0:
#                 materials.pop()
#                 values.popleft()
#             elif materials[-1] == 0:
#                 materials.pop()
#             elif values[0] == 0:
#                 values.popleft()
#
#
#
# if there_are_presents:
#     print(f"The presents are crafted! Merry Christmas!")
# else:
#     print(f"No presents this Christmas!")
#
# if materials:
#     materials_as_str = [str(m) for m in materials]
#     materials_as_str.reverse()
#     print(f"Materials left: {', '.join(materials_as_str)}")
# if values:
#     values_as_str = [str(v) for v in values]
#     print(f"Magic left: {', '.join(values_as_str)}")
# for toy, amount in sorted(toys.items()):
#     print(f"{toy}: {amount}")