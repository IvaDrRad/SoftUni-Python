employees_h = list(map(int, input().split()))
factor = int(input())
happy_employees = list(filter(lambda  emp: emp >= sum(employees_h) / len(employees_h), employees_h))

if len(happy_employees) >= len(employees_h) / 2:
    print(f'Score: {len(happy_employees)}/{len(employees_h)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(employees_h)}. Employees are not happy!')
