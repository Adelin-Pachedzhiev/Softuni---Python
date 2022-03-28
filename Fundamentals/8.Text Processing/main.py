# 1

# def check_length(string):
#     return 3 <= len(string) <= 16
#
#
# def check_letters(string:str):
#     for char in string:
#         if not(char.isalnum() or char == "-" or char=='_'):
#             return False
#     return True
#
#
# strings = input().split(", ")
# for string in strings:
#     if check_letters(string) and check_length(string):
#         print(string)

# 2
# longer_str, shorter_str = input().split(" ")
# sum = 0
#
# if len(longer_str) < len(shorter_str):
#     longer_str, shorter_str = shorter_str, longer_str
#
# extra_str = longer_str[len(shorter_str):len(longer_str)]
#
# for index in range(len(shorter_str)):
#     sum += ord(shorter_str[index]) * ord(longer_str[index])
#
# for index in range(len(extra_str)):
#     sum += ord(extra_str[index])
#
# print(sum)

# 3

# path = input().split("\\")
# file_name, file_extension = path.pop().split(".")
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")

# 4
# text = input()
# new_text =""
#
# for char in text:
#     new_text += chr(ord(char) + 3)
#
# print(new_text)

# 5
# text = input()
#
# for index in range(len(text)):
#     if text[index] == ":":
#         print(text[index:index + 2])

# 6
# text = input()
# new_text = text[0]
# for char in text:
#     if char != new_text[len(new_text) - 1]:
#         new_text += char
#
# print(new_text)

# 7
# text = input()
# chars_to_remove = 0
# new_text = ""
#
#
# for index in range(len(text)):
#     char = text[index]
#     if char == ">":
#         chars_to_remove += int(text[index + 1])
#         new_text += char
#         continue
#
#     if chars_to_remove > 0:
#         chars_to_remove -= 1
#         continue
#
#     new_text += char
#
# print(new_text)

# abv>1>1>2>2asdasd

# 8

# strings = input().split(" ")
# sum = 0
# for string in strings:
#     string = string.strip()
#     if string == "":
#         continue
#
#     first_letter = string[0]
#     number = int(string[1:len(string) - 1])
#     second_letter = string[len(string) - 1]
#
#     first_letter_alph_num = ord(first_letter.lower()) - 96
#     second_letter_alph_num = ord(second_letter.lower()) - 96
#
#     if first_letter == first_letter.upper():
#         number /= first_letter_alph_num
#     else:
#         number *= first_letter_alph_num
#
#     if second_letter == second_letter.upper():
#         number -= second_letter_alph_num
#     else:
#         number += second_letter_alph_num
#
#     sum += number
#
# print(f"{round(sum, 2):.2f}")

# 9

# text = input()
# new_text = ""
# chars_list = []
# string_so_far = ''
# for char in text:
#     if not char.lower().isnumeric() and char not in chars_list:
#         chars_list.append(char.lower())
#
#     if char.isnumeric():
#         new_text += string_so_far.upper() * int(char)
#         string_so_far = ""
#     else:
#         string_so_far += char
#
# print(f"Unique symbols used: {len(chars_list)}")
# print(new_text)

# 10

tickets = input().split(", ")

for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    winning_string = ""
    for index in range(round(len(ticket)/2)):
        char = ticket[index]
        if char == "@" or char == "#" or char == "$" or char == "^":
            winning_string += char

    if winning_string in ticket[round(len(ticket)/2) : len(ticket)]:
        if len(winning_string) == 10:
            print(f"ticket \"{ticket}\" - {len(winning_string)}{winning_string[0]} Jackpot!")
            continue
        elif 6 <= len(winning_string) <= 9 :
            print(f"ticket \"{ticket}\" - {len(winning_string)}{winning_string[0]}")
            continue
    print(f"ticket \"{ticket}\" - no match")


