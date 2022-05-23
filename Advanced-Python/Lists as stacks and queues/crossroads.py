from collections import deque

green_light_time = int(input())
free_window = int(input())

cars = deque()
cars_counter = 0
is_crashed = False

command = input()

while not command == "END":
    if command == "green":
        current_green = green_light_time
        while cars and current_green > 0:
            current_car = cars.popleft()
            if current_green >= len(current_car) or current_green + free_window >= len(current_car):
                cars_counter += 1
                current_green -= len(current_car)
            else:
                idx = free_window + current_green
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[idx]}.")
                is_crashed = True
                break
    else:
        cars.append(command)
    command = input()

if not is_crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")