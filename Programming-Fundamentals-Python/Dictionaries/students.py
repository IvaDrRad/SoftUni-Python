info = {}
students_info = input()
while ':' in students_info:
    command = students_info.split(':')
    name, student_id, course = command
    if course not in info:
        info[course] = {}
    info[course][student_id] = name
    students_info = input()

course = ' '.join(students_info.split('_'))
for key, value in info.items():
    if key == course:
        for stud_id, name in value.items():
            print(f'{name} - {stud_id}')

