symbols = input()
opening_brackets = []
balanced_brackets = True

if symbols.startswith(')') or symbols.startswith('}') or symbols.startswith(']'):
    print('NO')
else:
    for el in symbols:
        if el in '{[(':
            opening_brackets.append(el)
        else:
            to_pair = f'{opening_brackets.pop()}{el}'
            if to_pair not in '(){}[]':
                balanced_brackets = False
                break

if balanced_brackets:
    print('YES')
else:
    print('NO')
