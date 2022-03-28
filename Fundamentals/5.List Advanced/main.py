# 1

# list_1 = input().split(', ')
# list_2 = input().split(', ')
#
# list_result = []
#
# for element_1 in list_1:
#     for element_2 in list_2:
#         if (element_1 in element_2) and (element_1 not in list_result):
#             list_result.append(element_1)
# print(list_result)

# 2

# numbers = input().split(' ')
# numbers.sort()
# numbers.reverse()
# print(int(''.join(numbers)))

# 3

# version = list(map(int, input().split('.')))
# if version[2] + 1 > 9:
#     version[2] = 0
#
#     if version[1] + 1 > 9:
#
#         version[1] = 0
#         version[0] += 1
#
#     else:
#
#         version[1] += 1
#
# else:
#     version[2] += 1
#
# print(".".join(list(map(str, version))))

# 4

# room_count = int(input())
# free_chairs = 0
#
# for room_index in range(room_count):
#     room_info = input().split(" ")
#
#     num_chairs = len(room_info[0])
#     people_in_room = int(room_info[1])
#
#     if num_chairs < people_in_room:
#         needed_chairs = people_in_room - num_chairs
#         print(f"{needed_chairs} more chairs needed in room {room_index + 1}")
#         free_chairs -= needed_chairs
#     else:
#         free_chairs += (num_chairs - people_in_room)
# if free_chairs > 0:
#     print(f'Game On, {free_chairs} free chairs left')

# 5

# electrons = int(input())
# shells = []
# last_shell = 0
# shells.append(2 * (last_shell + 1) ** 2)
#
# while electrons > 0:
#     if shells[last_shell] < electrons:
#         electrons -= shells[last_shell]
#         last_shell += 1
#         shells.append(2 * (last_shell + 1) ** 2)
#     else:
#         shells[last_shell] = electrons
#         break
# print(shells)

# 6

# numbers = list(map(int, input().split(', ')))
# boundary = 0
#
# lists = []
#
# while len(numbers) > 0:
#     boundary += 10
#     lists.append([])
#     current_index = 0
#     while current_index != len(numbers):
#         if boundary - 10 < numbers[current_index] <= boundary:
#             lists[int(boundary / 10) - 1].append(numbers[current_index])
#             numbers.remove(numbers[current_index])
#         else:
#             current_index += 1
#
#
# for index in range(len(lists)):
#     print(f"Group of {(index + 1) * 10}'s: {lists[index]}")

# 7

# def swap_chars(word):
#     if len(word) == 1:
#         return word
#     else:
#         mid_of_string = word[1:len(word) - 1]
#         return word[len(word) - 1] + mid_of_string + word[0]
#
#
# message = input().split(' ')
# result_message = []
# for word in message:
#
#     char_code = ''
#     word_remain = ''
#
#     for char in word:
#         if 48 <= ord(char) <= 57:
#             char_code += char
#         else:
#             word_remain += char
#
#     char_code = chr(int(char_code))
#
#     result_message.append(char_code + swap_chars(word_remain))
# print(" ".join(result_message))


# 8
# def find_animal(animals, animal):
#     for index in range(len(animals)):
#         if animals[index][0] == animal:
#             return index
#     return -1
#
#
# def find_area(areas, area):
#     for index in range(len(areas)):
#         if areas[index][0] == area:
#             return index
#     return -1
#
#
# command = input()
# animals = []
# while command != "Last Info":
#     event, animal_name, food, area = command.split(':')
#     food = int(food)
#     animal_index = find_animal(animals, animal_name)
#
#     if event == "Add":
#
#         if animal_index == -1:
#             animals.append([animal_name, food, area])
#         else:
#             animals[animal_index][1] += food
#     else:
#         if animal_index != -1:
#             if (animals[animal_index][1] - food) <= 0:
#                 print(f"{animal_name} was successfully fed")
#                 animals.remove(animals[animal_index])
#             else:
#                 animals[animal_index][1] -= food
#     command = input()
# animals.sort(key=lambda elem: (-elem[1], elem[0]))
# print('Animals:')
# for animal in animals:
#     print(f'{animal[0]} -> {animal[1]}g')
#
# areas = []
# for element in animals:
#     index_area = find_area(areas, element[2])
#
#     if index_area == -1:
#         areas.append([element[2], 1])
#     else:
#         areas[index_area][1] += 1
#
# areas.sort(key=lambda elem: -elem[1])
# print('Areas with hungry animals:')
# for area in areas:
#     print(f'{area[0]} : {area[1]}')
