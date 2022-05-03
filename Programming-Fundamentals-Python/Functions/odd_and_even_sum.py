def digits_sum(number):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return even_sum, odd_sum


single_number = input()
even, odd = digits_sum(single_number)
print(f'Odd sum = {odd}, Even sum = {even}')