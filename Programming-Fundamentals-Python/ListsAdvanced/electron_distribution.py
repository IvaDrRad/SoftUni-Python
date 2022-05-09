number_of_electrons = int(input())
position_of_shell = 1
shells_distribution = []

while number_of_electrons > 0:
    fill_shells = 2 * (position_of_shell ** 2)
    if fill_shells <= number_of_electrons:
        shells_distribution.append(fill_shells)
        number_of_electrons -= fill_shells
    else:
        shells_distribution.append(number_of_electrons)
        break
    position_of_shell += 1

print(shells_distribution)




