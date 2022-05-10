words = input().split()
one_palindrome = input()
palindromes = [el for el in words if el == el[::-1]]
found_palindrome = [el for el in palindromes if el == one_palindrome]
print(palindromes)
print(f'Found palindrome {len(found_palindrome)} times')