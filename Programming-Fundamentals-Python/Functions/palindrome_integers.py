def palindrome_integers(numbers):
    for num in numbers:
        if num == num[::-1]:
            print(True)
        else:
            print(False)


list_of_numbers = input().split(', ')
# list_of_numbers = list(map(int, input().split(', ')))
palindrome_integers(list_of_numbers)


