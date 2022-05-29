from collections import deque

expression = deque(input().split())
current_state = deque()
operators = '*+-/'
new_number = 0

for el in expression:
    if el in operators:
        if el == '*':
            number = 1
            while current_state:
                new_number = current_state.popleft()
                number *= new_number
            current_state.append(number)
        elif el == '+':
            new_number = current_state.popleft()
            while current_state:
                new_number += current_state.popleft()
            current_state.append(new_number)
        elif el == '-':
            new_number = current_state.popleft()
            while current_state:
                new_number -= current_state.popleft()
            current_state.append(new_number)
        elif el == '/':
            new_number = current_state.popleft()
            while current_state:
                new_number /= current_state.popleft()
            current_state.append(int(new_number))
    else:
        current_state.append(int(el))

[print(el) for el in current_state]

