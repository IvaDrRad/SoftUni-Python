text = input()
occurrences = {}

for el in text:
    if el not in occurrences:
        occurrences[el] = 0
    occurrences[el] += 1

for match, times in sorted(occurrences.items()):
    print(f"{match}: {times} time/s")