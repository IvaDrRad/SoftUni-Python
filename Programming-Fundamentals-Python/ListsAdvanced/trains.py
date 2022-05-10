number_of_wagons = int(input())
train = [0] * number_of_wagons

command = input().split(" ")
while command[0] != 'End':
    if command[0] == 'add':
        train[len(train) - 1] += int(command[1])
    elif command[0] == 'insert':
        train[int(command[1])] += int(command[2])
    elif command[0] == 'leave':
        index, people = int(command[1]), int(command[2])
        train[index] -= int(people)
    command = input().split(" ")

print(train)