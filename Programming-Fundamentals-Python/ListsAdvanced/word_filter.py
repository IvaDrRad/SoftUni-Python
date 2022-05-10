some_text = input().split()
even_length = [word for word in some_text if len(word) % 2 == 0]
print(*even_length, sep='\n')