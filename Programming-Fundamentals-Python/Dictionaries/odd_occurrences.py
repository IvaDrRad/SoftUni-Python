words = input().split()
lower_words = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in lower_words:
        lower_words[word_lower] = 0
    lower_words[word_lower] += 1

for word, occur in lower_words.items():
    if occur % 2 != 0:
        print(word, end=' ')
