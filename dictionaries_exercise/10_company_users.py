command = input()
companies_users = {}

while command != 'End':
    info = command.split(' -> ')
    company = info[0]
    employ_id = info[1]

    if company not in companies_users:
        companies_users[company] = [employ_id]
    else:
        if employ_id not in companies_users[company]:
            companies_users[company].append(employ_id)

    command = input()

for company, employees in companies_users.items():
    print(f"{company}")
    for employ_id in employees:
        print(f"-- {employ_id}")
      
