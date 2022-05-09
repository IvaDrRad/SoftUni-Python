list_of_numbers = list(map(int, input().split(', ')))
boundary = 10

while len(list_of_numbers) > 0:
    result = [el for el in list_of_numbers if el <= boundary]
    print(f'Group of {boundary}\'s: {result}')
    list_of_numbers = [rest_el for rest_el in list_of_numbers if rest_el not in result]
    boundary += 10


# sequence_of_numbers = list(map(int, input().split(', ')))
# group_of_10s = []
# group_of_20s = []
# group_of_30s = []
# group_of_40s = []
# group_of_50s = []
# group_of_60s = []
# group_of_70s = []
# group_of_80s = []
# group_of_90s = []
#
# while True:
#     for num in sequence_of_numbers:
#         if num <= 10:
#             group_of_10s.append(num)
#             sequence_of_numbers.remove(num)
#         elif num <= 20:
#             group_of_20s.append(num)
#             sequence_of_numbers.remove(num)
#         elif num <= 30:
#             group_of_30s.append(num)
#             sequence_of_numbers.remove(num)
#         elif num <= 40:
#             group_of_40s.append(num)
#             sequence_of_numbers.remove(num)
#         elif num <= 50:
#             group_of_50s.append(num)
#             sequence_of_numbers.remove(num)
#         elif num <= 60:
#             group_of_60s.append(num)
#             sequence_of_numbers.remove(num)
#         elif num <= 70:
#             group_of_70s.append(num)
#             sequence_of_numbers.remove(num)
#         elif num <= 80:
#             group_of_80s.append(num)
#             sequence_of_numbers.remove(num)
#         elif num <= 90:
#             group_of_90s.append(num)
#             sequence_of_numbers.remove(num)
#
#     if len(sequence_of_numbers) == 0:
#         break
#     # group_of_10s = [num for num in sequence_of_numbers if num <= 10]
#     # group_of_20s = [num for num in sequence_of_numbers if 10 < num <= 20]
#     # group_of_30s = [num for num in sequence_of_numbers if 20 < num <= 30]
#     # group_of_40s = [num for num in sequence_of_numbers if 30 < num <= 40]
#     # group_of_50s = [num for num in sequence_of_numbers if 40 < num <= 50]
#
# print(f"Group of 10's: {group_of_10s}")
# print(f"Group of 20's: {group_of_20s}")
# print(f"Group of 30's: {group_of_30s}")
# print(f"Group of 40's: {group_of_40s}")
# if max(sequence_of_numbers) >= 40:
#     print(f"Group of 50's: {group_of_50s}")