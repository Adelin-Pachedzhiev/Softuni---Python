# 1

# n = int(input())
# user_names = set()
# for _ in range(n):
#     command = input()
#     if command not in user_names:
#         print(command)
#         user_names.add(command)


# 2

# n, m  = [int(num) for num in input().split(" ")]
#
# set_n = set()
# set_m = set()
#
# for _ in range(n):
#     set_n.add(input())
#
# for _ in range(m):
#     set_m.add(input())
#
# result_set = set_n & set_m
#
# for elem in result_set:
#     print(elem)

# 3

# lines = int(input())
# elements_set = set()
# for _ in range(lines):
#     input_line = input().split(" ")
#     for element in input_line:
#         if element not in elements_set:
#             print(element)
#             elements_set.add(element)

# 4

# text = input()
# char_dict = {}
# for char in text:
#     if char not in char_dict.keys():
#         char_dict[char] = 1
#     else:
#         char_dict[char] += 1
#
# char_keys = list(char_dict.keys())
# char_keys.sort()
# for char in char_keys:
#     print(f"{char}: {char_dict[char]} time/s")

# 5

# n = 0
# phonebook_dict = {}
# while True:
#     command = input()
#     if command.isnumeric():
#         n = int(command)
#         break
#
#     name, number = command.split('-')
#     phonebook_dict[name] = number
#
# for _ in range(n):
#     name = input()
#     if name in phonebook_dict.keys():
#         print(f"{name} -> {phonebook_dict[name]}")
#     else:
#         print(f"Contact {name} does not exist.")

# 6

n = int(input())
longest_intersection = set()
for _ in range(n):
    intervals = input().split("-")

    first_start, first_end = intervals[0].split(",")
    second_start, second_end = intervals[1].split(",")

    first_interval = set(range(int(first_start), int(first_end) + 1))
    second_interval = set(range(int(second_start), int(second_end) + 1))

    intersection = first_interval & second_interval
    if len(intersection) > len(longest_intersection):
       longest_intersection = intersection

print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")


