some_food = input().split()
food = {}

for i in range(0, len(some_food), 2):
    key = some_food[i]
    value = some_food[i + 1]
    food[key] = int(value)
print(food)