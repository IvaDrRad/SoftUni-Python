def add_user(forces_dict: dict, side, user):
    for side, users in forces_dict.items():
        if user in users:
            return forces_dict
    if side not in forces_dict:
        forces_dict[side] = [user]
    else:
        forces_dict[side].append(user)
    return forces_dict


force_book = {}
command = input()
while command != "Lumpawaroo":
    command_data = command.split(' | ')
    if len(command_data) > 1:
        force_side, force_user = command_data
        force_book = add_user(force_book, force_side, force_user)
    else:
        command = command.split(' -> ')
        force_user, force_side = command
    command = input()

a = 5