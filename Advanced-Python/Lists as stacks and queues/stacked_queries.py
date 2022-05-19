
number_of_queries = int(input())
stack = []
to_print = []

for _ in range(number_of_queries):
    current_query = input().split()
    if current_query[0] == '1':
        number = int(current_query[1])
        stack.append(number)
    elif current_query[0] == '2':
        if stack:
            stack.pop()
    elif current_query[0] == '3':
        if stack:
            print(max(stack))
    elif current_query[0] == '4':
        if stack:
            print(min(stack))


while stack:
    to_pop = str(stack.pop())
    to_print.append(to_pop)

print(', '.join(to_print))

