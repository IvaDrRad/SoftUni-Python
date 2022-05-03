grade = float(input())


def grades(type_of_grade):
    if type_of_grade < 3:
        return 'Fail'
    elif type_of_grade < 3.50:
        return 'Poor'
    elif type_of_grade < 4.50:
        return 'Good'
    elif type_of_grade < 5.50:
        return 'Very Good'
    elif type_of_grade >= 5.50:
        return 'Excellent'


print(grades(grade))
