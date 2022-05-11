courses = {}
command = input()
while command != 'end':
    course, student = command.split(' : ')
    if course not in courses:
        courses[course] = []
        courses[course].append(student)
    else:
        courses[course].append(student)
    command = input()

for key, value in courses.items():
    print(f"{key}: {len(courses[key])}")
    formatted = '\n-- '.join(value)
    print(f"-- {formatted}")