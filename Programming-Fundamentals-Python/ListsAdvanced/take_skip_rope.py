#
string_name = input()

number_list = []
string_list = []
take_list = []
skip_list = []
for i in range(len(string_name)):
    if string_name[i].isdigit():
        number_list.append(int(string_name[i]))
    else:
        string_list.append(string_name[i])

for x in range(len(number_list)):
    if x % 2 == 0:
        take_list.append(number_list[x])
    else:
        skip_list.append(number_list[x])

take_number = 0
skip_number = 0

index = 0
new_string = ""

for i in range(len(take_list)):
    take_number=take_list[i]
    skip_number=skip_list[i]
    new_string+="".join(string_list[:take_number])
    del string_list[0:take_number+skip_number]

print(new_string)
# # мое решение - не е довършено
# some_string = input()
#
# only_digits = [int(num) for num in some_string if num.isdigit()]
# non_numbers = ""
#
# for el in some_string:
#     if not el.isdigit():
#         non_numbers += el
#
# take_list = [only_digits[i] for i in range(len(only_digits)) if i % 2 == 0]
# skip_list = [only_digits[i] for i in range(len(only_digits)) if i % 2 != 0]
# result_string = ''
# position = len(skip_list)
# counter = 0
# while True:
#     if position == 0:
#         break
#
#     for el_1 in take_list:
#         counter = 0
#         counter += el_1 - 1
#         current_count_to_take = non_numbers[:el_1]
#         non_numbers = non_numbers.replace(current_count_to_take, '', 1)
#         result_string += current_count_to_take
#         for el_2 in skip_list:
#             position -= 1
#             to_skip = non_numbers[:el_2]
#             non_numbers = non_numbers.replace(to_skip, '', 1)
#             break
#
#
# print(result_string)
