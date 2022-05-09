numbers_list = input().split()
rounded_list = []
for num in numbers_list:
    current_number = float(num)
    rounded_list.append(round(current_number))

print(rounded_list)
