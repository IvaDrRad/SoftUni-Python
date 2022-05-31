number_of_guests = int(input())

regular_guests = set()
vip_guests = set()

for _ in range(number_of_guests):
    res_code = input()
    if res_code[0].isdigit():
        vip_guests.add(res_code)
    else:
        regular_guests.add(res_code)

while True:
    guest = input()
    if guest == "END":
        break
    elif guest[0].isdigit():
        vip_guests.remove(guest)
    else:
        regular_guests.remove(guest)

total_guests_no_show = len(vip_guests) + len(regular_guests)
print(total_guests_no_show)
[print(guest) for guest in sorted(vip_guests)]
[print(guest) for guest in sorted(regular_guests)]
# print('\n'.join(sorted(vip_guests))) <-- така изписано е по-бавно!
# print('\n'.join(sorted(regular_guests)))