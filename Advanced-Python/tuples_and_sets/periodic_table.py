count = int(input())
ch_elements = set()

for _ in range(count):
    elements = input().split()
    for el in elements:
        ch_elements.add(el)

[print(el) for el in ch_elements]