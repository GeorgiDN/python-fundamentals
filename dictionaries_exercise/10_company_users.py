def company_users():
    companies_info = {}

    while True:
        command = input()
        if command == "End":
            break

        data = command.split(" -> ")
        company_name, employ_id = data[0], data[1]

        if company_name not in companies_info:
            companies_info[company_name] = []

        if employ_id not in companies_info[company_name]:
            companies_info[company_name].append(employ_id)

    for company, id_data in companies_info.items():
        print(f"{company}")
        for id_ in id_data:
            print(f"-- {id_}")

    return companies_info


company_users()





# command = input()
# companies_users = {}

# while command != 'End':
#     info = command.split(' -> ')
#     company = info[0]
#     employ_id = info[1]

#     if company not in companies_users:
#         companies_users[company] = [employ_id]
#     else:
#         if employ_id not in companies_users[company]:
#             companies_users[company].append(employ_id)

#     command = input()

# for company, employees in companies_users.items():
#     print(f"{company}")
#     for employ_id in employees:
#         print(f"-- {employ_id}")
      
