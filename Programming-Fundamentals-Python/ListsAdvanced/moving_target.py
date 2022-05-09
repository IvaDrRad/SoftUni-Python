# 90/100 в judge има още едно решение със 100/100

targets = list(map(int, input().split()))

command = input()
while command != 'End':
    command = command.split(' ')
    index = int(command[1])
    if command[0] == 'Shoot':
        power = int(command[2])
        if index in range(len(targets)):
            targets[index] -= power
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif command[0] == 'Add':
        value = int(command[2])
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print(f'Invalid placement!')
    elif command[0] == 'Strike':
        radius = int(command[2])
        if (index - radius) in range(len(targets)) and index in range(len(targets)) and (index + radius) in range(len(targets)):
            items_to_remove = [targets[index - radius], targets[index], targets[index + radius]]
            targets = [el for el in targets if el not in items_to_remove]
        else:
            print('Strike missed!')
    command = input()
# result = f"'|' + {targets}"
print(*targets, sep='|')