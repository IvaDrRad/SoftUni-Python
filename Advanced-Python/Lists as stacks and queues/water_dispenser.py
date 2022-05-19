from collections import deque

water_quantity = int(input())
action = input()
people = deque()

while action != "Start":
    people.append(action)
    action = input()

action = input()
while action != "End":
    if action.startswith("refill"):
        action = action.split()
        liters = int(action[1])
        water_quantity += liters
    else:
        liters = int(action)
        person_for_water = people.popleft()
        if liters <= water_quantity:
            print(f"{person_for_water} got water")
            water_quantity -= liters
        else:
            print(f"{person_for_water} must wait")
    action = input()

print(f"{water_quantity} liters left")