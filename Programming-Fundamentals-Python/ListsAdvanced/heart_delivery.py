even_integers = list(map(int, input().split('@')))
current_position = 0
command = input().split()
while command[0] != 'Love!':
    length = int(command[1])
    current_position += length
    if current_position not in range(len(even_integers)):
        current_position = 0
    if even_integers[current_position] == 0:
        print(f"Place {current_position} already had Valentine's day.")
    else:
        even_integers[current_position] -= 2
        if even_integers[current_position] == 0:
            print(f"Place {current_position} has Valentine's day." )
    command = input().split()

print(f"Cupid's last position was {current_position}.")
check_if_true = [el for el in even_integers if el != 0]
if len(check_if_true) > 0:
    print(f'Cupid has failed {len(check_if_true)} places.')
else:
    print('Mission was successful.')

