symbols = input()
opening_brackets = []
balanced_brackets = True

# if symbols.startswith(')') or symbols.startswith('}') or symbols.startswith(']'):
#     print('NO')
pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}

for el in symbols:
    if el in '{[(':
        opening_brackets.append(el)
    elif not opening_brackets:
        balanced_brackets = False

    else:
        to_pair = f'{opening_brackets.pop()}{el}'
        if to_pair not in '(){}[]':
            balanced_brackets = False
    if not balanced_brackets:
        break

if not balanced_brackets or opening_brackets:
    print('NO')
else:
    print('YES')

# symbols = input()
# opening_brackets = []
# balanced_brackets = True
#
# if symbols.startswith(')') or symbols.startswith('}') or symbols.startswith(']'):
#     print('NO')
# else:
#     for el in symbols:
#         if el in '{[(':
#             opening_brackets.append(el)
#         elif not opening_brackets:
#
#         else:
#             to_pair = f'{opening_brackets.pop()}{el}'
#             if to_pair not in '(){}[]':
#                 balanced_brackets = False
#                 break
#
# if not balanced_brackets or opening_brackets:
#     print('NO')
# else:
#     print('YES')