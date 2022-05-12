phone_book = {}
while True:
    contact = input()
    if '-' not in contact:
        break
    else:
        current_name, phone_number = contact.split('-')
        phone_book[current_name] = phone_number
print(phone_book)
number = int(contact)
for _ in range(number):
    searched_name = input()
    if searched_name in phone_book:
        print(f"{searched_name} -> {phone_book[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
