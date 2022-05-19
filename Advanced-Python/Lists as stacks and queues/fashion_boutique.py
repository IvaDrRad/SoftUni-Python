box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
counter_of_racks = 1
current_space = rack_capacity

while box_of_clothes:
    current_cloth = box_of_clothes[-1]
    if current_cloth > current_space:
        counter_of_racks += 1
        current_space = rack_capacity
    else:
        current_space -= current_cloth
        box_of_clothes.pop()

print(counter_of_racks)
