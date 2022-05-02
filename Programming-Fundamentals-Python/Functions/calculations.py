operator = input()
number_1 = int(input())
number_2 = int(input())


def calculator_of_numbers(first_number, second_number):
    if operator == 'multiply':
        return first_number * second_number
    if operator == 'divide':
        return int(first_number / second_number)
    if operator == 'add':
        return first_number + second_number
    if operator == 'subtract':
        return first_number - second_number

print(calculator_of_numbers(number_1, number_2))


