def password_check(password):
    validator = True
    special_sum = ['$', '@', '#']
    special_characters = ['$', '#', '@', '!', '*']
    if 6 > len(password) or len(password) > 10:
        validator = False
        print('Password must be between 6 and 10 characters')
    if not str.isalnum(password) and not str.isdigit(password):
        validator = False
        print(f'Password must consist only of letters and digits')
    if len([x for x in password if x.isdigit()]) < 2:
        validator = False
        print(f'Password must have at least 2 digits')
    if validator:
        print(f"Password is valid")
# less than 2 digits


input_password = input()
password_check(input_password)


