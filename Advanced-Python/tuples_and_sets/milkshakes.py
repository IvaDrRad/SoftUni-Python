from collections import deque

chocolate = [int(el) for el in input().split(', ')]
milk = deque([int(el) for el in input().split(', ')])
total_milkshakes = 0
success = False

while chocolate and milk:
    if chocolate[-1] <= 0 or milk[0] <= 0:
        if chocolate[-1] <= 0:
            chocolate.pop()
        if milk[0] <= 0:
            milk.popleft()
        if len(chocolate) == 0 or len(milk) == 0:
            break
    elif chocolate[-1] == milk[0]:
        total_milkshakes += 1
        chocolate.pop()
        milk.popleft()
        if total_milkshakes == 5:
            success = True
            break
    else:
        milk.append(milk.popleft())
        chocolate[-1] -= 5

if success:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(choco) for choco in chocolate])}")
else:
    print(f"Chocolate: empty")
if milk:
    print(f"Milk: {', '.join([str(milk) for milk in milk])}")
else:
    print(f"Milk: empty")
