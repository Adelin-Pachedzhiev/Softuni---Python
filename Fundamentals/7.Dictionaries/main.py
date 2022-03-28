# 1
# from _collections import defaultdict
#
# text = input()
# result = defaultdict(int)
# for char in text:
#     result[char] += 1
#
# for key in result.keys():
#     if key == " ":
#         continue
#     print(f"{key} -> {result[key]}")

# 2
# from _collections import defaultdict
#
# resources = defaultdict(int)
# while True:
#     key = input()
#     if key == "stop":
#         break
#     quantity = int(input())
#     resources[key] += quantity
#
# for key in resources.keys():
#     print(f'{key} -> {resources[key]}')

# 3
# from _collections import defaultdict
#
# junk_items = defaultdict(int)
# legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
#
# is_done = False
#
# while not is_done:
#     row = input().split(' ')
#     for index in range(0, len(row), 2):
#         item_quality = int(row[index])
#         item_name = row[index + 1].lower()
#         if item_name == "shards" or item_name == "fragments" or item_name == "motes":
#             legendary_items[item_name] += int(item_quality)
#
#             if legendary_items[item_name] >= 250:
#
#                 legendary_items[item_name] -= 250
#
#                 if item_name == "shards":
#                     print(f"Shadowmourne obtained!")
#                 elif item_name == "fragments":
#                     print(f"Valanyr obtained!")
#                 elif item_name == "motes":
#                     print(f"Dragonwrath obtained!")
#
#                 is_done = True
#                 break
#         else:
#             junk_items[item_name] += int(item_quality)
#
# legendary_items = list(legendary_items.items())
# legendary_items.sort(key =  lambda item: (-item[1], item[0]))
# for item in legendary_items:
#     print(f"{item[0]}: {item[1]}")
#
# junk_items = list(junk_items.items())
# junk_items.sort(key = lambda item: item[0])
# for item in junk_items:
#     print(f"{item[0]}: {item[1]}")

# 4.
# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
# items_dict = {}
#
# while True:
#     command = input()
#     if command == "buy":
#         break
#     item_name, item_price, item_quantity = command.split(' ')
#     item_price = float(item_price)
#     item_quantity = int(item_quantity)
#
#     item = Item(item_name, item_price, item_quantity)
#     if item.name in items_dict.keys():
#         items_dict[item.name].quantity += item.quantity
#         items_dict[item.name].price = item.price
#     else:
#         items_dict[item.name] = item
#
# for item in items_dict.values():
#     print(f'{item.name} -> {(item.price*item.quantity):.2f}')

# 5.

# command_count = int(input())
# parking_lot = {}
# for _ in range(command_count):
#     command = input().split(' ')
#     if command[0] == "register":
#         username = command[1]
#         licensePlate = command[2]
#         if username in parking_lot.keys():
#             print(f'ERROR: already registered with plate number {parking_lot[username]}')
#             continue
#         parking_lot[username] = licensePlate
#         print(f'{username} registered {licensePlate} successfully')
#     else:
#         username = command[1]
#         if username not in parking_lot.keys():
#             print(f'ERROR: user {username} not found')
#             continue
#         del parking_lot[username]
#         print(f'{username} unregistered successfully')
#
# for user in parking_lot.items():
#     print(f'{user[0]} => {user[1]}')

# 6.

# courses = {}
#
# while True:
#     command = input()
#     if command == "end":
#         break
#
#     courseName, studentName = command.split(" : ")
#
#     if courseName not in courses.keys():
#         courses[courseName] = []
#
#     courses[courseName].append(studentName)
#
# coursesList = list(courses.items())
# coursesList.sort(key = lambda elem: -len(elem[1]))
# for course in coursesList:
#     courseName = course[0]
#     courseMembers = course[1]
#     print(f"{courseName}: {len(courseMembers)}")
#
#     courseMembers.sort()
#     for student in courseMembers:
#         print(f"-- {student}")

# 7

# count = int(input())
# students = {}
# for _ in range(count):
#     studentName = input()
#     studentGrade = float(input())
#     if studentName not in students.keys():
#         students[studentName] = []
#     students[studentName].append(studentGrade)
#
# for student in students.items():
#     studentName = student[0]
#     studentGrades = student[1]
#
#     average = sum(studentGrades) / len(studentGrades)
#     del students[studentName]
#
#     if average >= 4.5:
#         students[studentName] = average
#
# students_list = list(students.items())
# students_list.sort(key = lambda studentInfo: -studentInfo[1])
#
# for student in students_list:
#     print(f"{student[0]} –> {student[1]}")

# 8

# companies = {}
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     companyName, employeeId = command.split(' -> ')
#     if companyName not in companies.keys():
#         companies[companyName] = []
#
#     if employeeId not in companies[companyName]:
#         companies[companyName].append(employeeId)
#
# companies_list = list(companies.items())
# companies_list.sort(key = lambda company: company[0])
#
# for company in companies_list:
#     companyName = company[0]
#     empleyeesId = company[1]
#     print(companyName)
#     for employee in empleyeesId:
#         print(f'-- {employee}')

# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End

# 9

# def check_existing_user(forceSides:dict, forceUser):
#
#     for side, users in forceSides.items():
#         if forceUser in users:
#             return side
#     return -1
#
#
# forceSides = {}
#
# while True:
#     row_input = input()
#     if row_input == "Lumpawaroo":
#         break
#
#     if " | " in row_input:
#         forceSide, forceUser = row_input.split(" | ")
#         if forceSide not in forceSides.keys():
#             forceSides[forceSide] = []
#         if forceUser not in forceSides[forceSide]:
#             forceSides[forceSide].append(forceUser)
#     else:
#         forceUser, forceSide = row_input.split(" -> ")
#         userSide = check_existing_user(forceSides, forceUser)
#
#         if userSide == -1:
#             forceSides[forceSide].append(forceUser)
#         else:
#             forceSides[userSide].remove(forceUser)
#             forceSides[forceSide].append(forceUser)
#         print(f"{forceUser} joins the {forceSide} side!")
#
# forceSides_list = list(forceSides.items())
# forceSides_list.sort(key = lambda item: (len(item[1]), item[0]))
# for force in forceSides_list:
#     forceSide, users = force
#     if len(users) > 0:
#         print(f"Side: {forceSide}, Members: {len(users)}")
#         users.sort()
#         for user in users:
#             print(f"! {user}")


# Lighter | Royal
# Darker | DCay
# Ivan Ivanov -> Lighter
# DCay -> Lighter
# Lumpawaroo

# 10



user_points_dict = {}
submissions_dict = {}


while True:
    command = input().split('-')
    if command[0] == 'exam finished':
        break

    if command[1] == "banned":
        userName = command[0]
        del user_points_dict[userName]
        continue

    userName, language, points = command
    points = int(points)

    if userName not in user_points_dict.keys():
        user_points_dict[userName] = points

    if language not in submissions_dict.keys():
        submissions_dict[language] = 0
    submissions_dict[language] += 1

user_points_list = list(user_points_dict.items())
user_points_list.sort(key = lambda items: (-items[1], items[0]))

print("Results:")
for userName,points in user_points_list:
    print(f"{userName} | {points}")

submissions_list = list(submissions_dict.items())
submissions_list.sort(key = lambda items: (-items[1], items[0]))

print("Submissions:")
for language,submissionsCount in submissions_list:
    print(f"{language} - {submissionsCount}")







