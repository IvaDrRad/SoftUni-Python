some_numbers = list(map(int, input().split(', ')))
positives = []
negatives = []
even = []
odds = []

for number in some_numbers:
    if number >= 0:
        positives.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odds.append(number)
    if number < 0:
        negatives.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odds.append(number)
positives = ', '.join(str(el) for el in positives)
negatives = ', '.join(str(el) for el in negatives)
even = ', '.join(str(el) for el in even)
odds = ', '.join(str(el) for el in odds)
print(f"Positive: {positives}")
print(f"Negative: {negatives}")
print(f"Even: {even}")
print(f"Odd: {odds}")

