list_of_chars = input().split(", ")
chars_dict = {el: ord(el) for el in list_of_chars}
print(chars_dict)