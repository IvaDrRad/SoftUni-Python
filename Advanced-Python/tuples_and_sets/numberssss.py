first_row = set([int(x) for x in set(input().split())])
second_row = set([int(x) for x in set(input().split())])
number = int(input())

for _ in range(number):
    command = input().split()
    if command[0] == 'Add':
        if command[1] == 'First':
            to_add = set([int(x) for x in command[2:len(command)]])
            first_row = first_row | to_add
        else:
            to_add = set([int(x) for x in command[2:len(command)]])
            second_row = second_row | to_add
    elif command[0] == 'Remove':
        if command[1] == 'First':
            first_row = first_row - set([int(x) for x in command[2:len(command)]])
        else:
            second_row = second_row - set([int(x) for x in command[2:len(command)]])
    elif command[0] == 'Check':
        if first_row < second_row or second_row < first_row:
            print("True")
        else:
            print("False")

first_row = sorted(first_row)
second_row = sorted(second_row)
print(', '.join(str(el) for el in first_row))
print(', '.join(str(el) for el in second_row))