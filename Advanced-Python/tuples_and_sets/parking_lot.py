number = int(input())
cars_info = set()

for _ in range(number):
    command, current_car = input().split(', ')
    if command == 'IN':
        if current_car not in cars_info:
            cars_info.add(current_car)
    elif command == 'OUT':
        if current_car in cars_info:
            cars_info.remove(current_car)

if cars_info:
    print('\n'.join(cars_info))
else:
    print("Parking Lot is Empty")