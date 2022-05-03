def multiplication_sign(num_1, num_2, num_3):
    if num_1 == 0 or num_2 == 0 or num_3 == 0:
        print('zero')
    elif num_1 < 0 or num_2 < 0 or num_3 < 0:
        counter = 0
        if num_1 < 0:
            counter +=1
        if num_2 <0:
            counter +=1
        if num_3 < 0:
            counter += 1
        if counter % 2 != 0:
            print('negative')
        else:
            print('positive')
    else:
        print('positive')


first_number = int(input())
second_number = int(input())
third_number = int(input())
multiplication_sign(first_number, second_number, third_number)