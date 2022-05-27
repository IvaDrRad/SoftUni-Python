number_of_students = int(input())
students_info = {}

for _ in range(number_of_students):
    student_name, grade = input().split(' ')
    if student_name not in students_info:
        students_info[student_name] = []
    students_info[student_name].append(float(grade))

for student, grades in students_info.items():
    average = sum(grades) / len(grades)
    to_print = f"{' '.join([f'{x:.2f}' for x in grades])}"
    print(f"{student} -> {to_print} (avg: {average:.2f})")