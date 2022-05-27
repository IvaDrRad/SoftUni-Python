numbers = int(input())
names = set()

for _ in range(numbers):
    name = input()
    names.add(name)

print('\n'.join(names))