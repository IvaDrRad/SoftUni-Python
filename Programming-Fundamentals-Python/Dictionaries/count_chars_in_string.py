result = {}
text = input()
counter = 0
for l in text:
    if l == ' ':
        continue
    else:
        if l not in result:
            counter = 1
            result[l] = counter
        else:
            result[l] += 1

for k, v in result.items():
    print(f"{k} -> {v}")

