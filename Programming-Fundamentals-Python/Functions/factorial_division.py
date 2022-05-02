def factorial_1(number_1):

    if number_1 == 0:
        fact_num_1 = 1
    else:
        fact_num_1 = number_1 * factorial_1(number_1-1)
    return fact_num_1


def factorial_2(number_2):
    if number_2 == 0:
        fact_num_2 = 1
    else:
        fact_num_2 = number_2 * factorial_2(number_2 - 1)
    return fact_num_2


first_number = int(input())
second_number = int(input())
result = factorial_1(first_number) / factorial_2(second_number)
print(f'{result:.2f}')
