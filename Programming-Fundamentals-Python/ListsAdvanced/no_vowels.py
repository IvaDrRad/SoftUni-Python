text = input()
vowels = 'a', 'o', 'u', 'e', 'i'
no_vowels = ''.join([letter for letter in text if str.lower(letter) not in vowels])
print(no_vowels)