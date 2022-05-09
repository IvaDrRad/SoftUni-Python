def perfect_number(number):
    counter = 0
    is_perfect = False
    for nums in range(1, int(number)):
        if int(number) % int(nums) == 0:
            counter += int(nums)
    if counter == int(number):
        is_perfect = True
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


num = input()
perfect_number(num)


