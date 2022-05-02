numbers = input().split()
abs_values = []
for number in numbers:
    current_number = float(number)
    abs_values.append(abs(current_number))

print(abs_values)