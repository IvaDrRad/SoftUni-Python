# def add_user(forces_as_dict, to_side, user_to_be_added):
#     for side, users in forces_as_dict:
#         if user_to_be_added in users:
#             return forces_as_dict
#     if to_side not in forces_as_dict:
#         forces_as_dict[to_side] = user_to_be_added
#     else:
#         forces_as_dict[to_side].append(user_to_be_added)
#     return forces_as_dict


force_book = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(' | ')
        # force_book = add_user(force_book, force_side, force_user)
        if force_side not in force_book:
            force_book[force_side] = []
            if force_user not in force_book[force_side]:
                force_book[force_side].append(force_user)
        else:
            if force_user not in force_book.values():
                force_book[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(' -> ')
        for side, user in force_book.items():
            if force_side not in force_book and force_user not in force_book.values():
                force_book[force_side] = []
                force_book[force_side].append(force_user)
            elif force_user not in force_book.values():
                force_book[force_side] = force_user
                print(f"{force_user} joins the {force_side} side!")
            elif force_user in force_book.values():
                for side, user in force_book.items():
                    force_book[force_side].remove(force_user)
                if force_side not in force_book and force_user not in force_book.values():
                    force_book[force_side] = []
                    force_book[force_side].append(force_user)
                elif force_user not in force_book.values():
                    force_book[force_side] = force_user
                    print(f"{force_user} joins the {force_side} side!")
    command = input()
for side, users in force_book.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        print(f"'! '.join{users}")
