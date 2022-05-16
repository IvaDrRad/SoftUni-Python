number = int(input())
grades = {}
for _ in range(number):
    student_name = input()
    student_grade = float(input())
    if student_name not in grades:
        grades[student_name] = []
    grades[student_name].append(student_grade)

filtered_grades = {}

for student_name, student_grade in grades.items():
    avg_grade = sum(student_grade) / len(student_grade)
    if avg_grade >= 4.50:
        filtered_grades[student_name] = avg_grade

for name, grade in filtered_grades.items():
    print(f"{name} -> {grade:.2f}")

