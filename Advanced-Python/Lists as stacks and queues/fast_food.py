from collections import deque

food_quantity = int(input())
orders = deque([int(el) for el in input().split()])
enough_food = True

print(max(orders))

while orders:
    if food_quantity - orders[0] >= 0:
        food_quantity -= orders[0]
        orders.popleft()

    else:
        enough_food = False
        break

if enough_food:
    print("Orders complete")
else:
    to_print = 'Orders left: '
    for el in orders:
        to_print += f'{str(el)} '
    print(''.join(to_print))