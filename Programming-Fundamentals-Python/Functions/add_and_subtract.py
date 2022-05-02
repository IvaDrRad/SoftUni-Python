first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(num1, num2):
    return num1 + num2


def subtract(sum, num3):
    return sum - num3


print(subtract(sum_numbers(first_number, second_number), third_number))


