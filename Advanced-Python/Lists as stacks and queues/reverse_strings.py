input_string = list(input())

while input_string:
    reversed = input_string.pop()
    print(reversed, end='')

# мой вариант 2:
# string = input().split()
# reversed_string = []
#
# while string:
#     for word in string:
#         element_to_pop = string.pop()
#         reversed_string.append(element_to_pop[::-1])
#
# print(" ".join(reversed_string))

# oт лекциите:
# text = list(input())
# stack = []
#
# for i in range(len(text)):
#     stack.append(text.pop())
#
# print("".join(stack))
