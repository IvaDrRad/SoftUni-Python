first_char = input()
last_char = input()


def ascii_table(char_1, char_2):
    string_of_chars = ''
    for char in range(ord(char_1) + 1, ord(char_2)):
        current_symbol = chr(char)
        string_of_chars += f"{current_symbol} "
    return string_of_chars


print(ascii_table(first_char, last_char))