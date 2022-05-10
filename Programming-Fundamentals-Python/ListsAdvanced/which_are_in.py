first_sequence = input().split(', ')
second_sequence = input()
result = [el for el in first_sequence if el in second_sequence]

print(result)