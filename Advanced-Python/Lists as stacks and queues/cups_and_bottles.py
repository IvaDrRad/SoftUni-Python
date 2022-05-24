from collections import deque

cups_capacity_l = deque([int(x) for x in input().split()])
filled_bottles = [int(x) for x in input().split()]
wasted_litters = 0
current_bottle = 0

while cups_capacity_l or filled_bottles:
    if len(cups_capacity_l) == 0 or len(filled_bottles) == 0:
        break
    else:
        bottle = filled_bottles[-1]
        cup = cups_capacity_l[0]
        if cup > bottle:
            while cup > 0 and len(filled_bottles) > 0:
                current_bottle = filled_bottles.pop()
                if current_bottle > cup:
                    cup -= current_bottle
                    wasted_litters += abs(cup)
                else:
                    cup -= current_bottle
            cups_capacity_l.popleft()

        else:
            left_litters = bottle - cup
            wasted_litters += left_litters
            filled_bottles.pop()
            cups_capacity_l.popleft()


if len(filled_bottles) > 0:
    bottles = f'Bottles: '
    while filled_bottles:
        bottles += str(filled_bottles.pop())
    print(f"{bottles}")
    print(f"Wasted litters of water: {wasted_litters}")
if len(cups_capacity_l) > 0:
    cups = f'Cups: '
    while cups_capacity_l:
        cups += f"{str(cups_capacity_l.popleft())} "
    print(f"{cups}")
    print(f"Wasted litters of water: {wasted_litters}")


