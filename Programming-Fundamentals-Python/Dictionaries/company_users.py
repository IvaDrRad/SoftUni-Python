company_users = {}
command = input()
while command != 'End':
    company, user_id = command.split(' -> ')
    if company not in company_users:
        company_users[company] = []
    if user_id not in company_users[company]:
        company_users[company].append(user_id)
    command = input()

for company, user in company_users.items():
    print(f"{company}")
    for user_id in user:
        print(f"-- {user_id}")