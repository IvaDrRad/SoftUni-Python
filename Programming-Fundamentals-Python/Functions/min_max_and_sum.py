def min_max_sum(some_list_of_numbers):
    print(f"The minimum number is {min(some_list_of_numbers)}")
    print(f"The maximum number is {max(some_list_of_numbers)}")
    print(f"The sum number is: {sum(some_list_of_numbers)}")


numbers_as_digits = list(map(int, input().split()))
min_max_sum(numbers_as_digits)

