# 1
# first_num = int(input())
# second_num = int(input())
# divider = int(input())
# multiplier = int(input())
# result = int((first_num + second_num) / divider )
# result = int(result * multiplier)
# print(result)

# 2
# first_char = input()
# second_char = input()
# third_char = input()
# print(first_char+second_char+third_char)

# 3
# people = int(input())
# capacity = int(input())
# result = int(people / capacity)
# if people % capacity:
#     result = int(result) + 1
# print(result)

# 4
# n = int(input())
# result = 0
# for index in range(0, n):
#     char = input()
#     result += ord(char)
# print(f"The sum equals: {result}")

# 5
# start_index = int(input())
# end_index = int(input())
# result = ""
# for num in range(start_index, end_index + 1):
#     print(chr(num), end=" " )

# 6
# n_letters = int(input())
# for first_chr in range(97, 97 + n_letters):
#     for second_chr in range(97, 97 + n_letters):
#         for third_chr in range(97, 97 + n_letters):
#             print(chr(first_chr) + chr(second_chr) + chr(third_chr))

# 7
# interval = int(input())
# tank_capacity = 255
# filled_space = 0
# for index in range(0, interval):
#     quantity = int(input())
#     if filled_space + quantity > tank_capacity:
#         print("Insufficient capacity!")
#         continue
#     filled_space += quantity
# print(filled_space)

# 8
# party_size = int(input())
# days = int(input())
# earnings = 0
# for day in range(1, days + 1):
#     if day % 10 == 0:
#         party_size -= 2
#     if day % 15 == 0:
#         party_size += 5
#
#     earnings += 50
#     earnings -= 2 * party_size
#
#     if day % 3 == 0:
#         earnings -= 3 * party_size
#     if day % 5 == 0:
#         earnings += 20 * party_size
#         if day % 3 == 0:
#             earnings -= 2 * party_size
# print(f"{party_size} companions received {int(earnings / party_size)} coins each.")

# 9
# sn_number = int(input())
#
# snowball_snow = int(input())
# snowball_time = int(input())
# snowball_quality = int(input())
#
# snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)
#
# snowball_max_snow = snowball_snow
# snowball_max_time = snowball_time
# snowball_max_quality = snowball_quality
#
# snowball_max_value = snowball_value
#
# for snowball in range(1, sn_number):
#
#     snowball_snow = int(input())
#     snowball_time = int(input())
#     snowball_quality = int(input())
#
#     snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)
#
#     if snowball_value > snowball_max_value:
#         snowball_max_snow = snowball_snow
#         snowball_max_time = snowball_time
#         snowball_max_quality = snowball_quality
#
#         snowball_max_value = snowball_value
# print(f"{snowball_max_snow} : {snowball_max_time} = {snowball_max_value} ({snowball_max_quality})")