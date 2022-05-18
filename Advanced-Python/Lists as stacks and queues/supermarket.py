from collections import deque

command = input()
queue = deque()

while command != "End":
    if command == 'Paid':
        while queue:
            to_print = queue.popleft()
            print(to_print)
    else:
        queue.append(command)
    command = input()

print(f"{len(queue)} people remaining.")

