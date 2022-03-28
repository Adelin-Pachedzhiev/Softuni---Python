# 1
# def find_smallest_num(number1, number2, number3):
#     smallest_num = number1
#     if number2 < smallest_num:
#         smallest_num = number2
#     if number3 < smallest_num:
#         smallest_num = number3
#     return smallest_num
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# print(find_smallest_num(num1, num2, num3))

# 2
# def add_and_substract(num1, num2, num3):
#
#     def sum_numbers(number1, number2):
#         return number1 + number2
#
#
#     def subtract(number1, number2):
#         return number1 - number2
#
#     return subtract(sum_numbers(num1, num2), num3)
#
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
#
# print(add_and_substract(number1, number2, number3))

# 3

# def characters_in_range(str1, str2):
#     result = ""
#     for char in range(ord(str1) + 1, ord(str2)):
#         result+= (chr(char) + " ")
#     return result
#
# string1 = input()
# string2 = input()
#
# print(characters_in_range(string1, string2))

# 4

# def sum_even_odd(number):
#     number = str(number)
#     even_sum = 0
#     odd_sum = 0
#
#     for digit in number:
#         digit = int(digit)
#         if digit % 2 == 0:
#             even_sum += digit
#         else:
#             odd_sum += digit
#
#     result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
#     return result
#
#
# number = int(input())
# print(sum_even_odd(number))


# 5

# def is_palindrome(str):
#     return str == str[::-1]
#
#
# str_numbers = input().split(", ")
#
# for num in str_numbers:
#     print(is_palindrome(num))

# 6

# def check_length(password):
#     if not(6 <= len(password) <= 10):
#         print("Password must be between 6 and 10 characters")
#         return False
#     return True
#
#
# def check_letters_digits(password):
#     for char in password:
#         if not ((65 <= ord(char) <= 90) or (97 <= ord(char) <= 122) or (48 <= ord(char) <= 57)):
#             print("Password must consist only of letters and digits")
#             return False
#     return True
#
#
# def check_for_digits(password):
#     digits = 0
#     for char in password:
#         if  48 <= ord(char) <= 57:
#             digits += 1
#     if digits < 2:
#         print("Password must have at least 2 digits")
#         return False
#     return True
#
# password = input()
#
# checked_length = check_length(password)
# checked_letters_digits = check_letters_digits(password)
# checked_for_digits = check_for_digits(password)
# if checked_length and checked_letters_digits and checked_for_digits:
#      print("Password is valid")

# 7
#
# def perfect_number(number):
#     divisor_sum = 0
#     for divisor in range(1, number):
#         if number % divisor == 0:
#             divisor_sum += divisor
#     return number == divisor_sum
#
# input_number = int(input())
# if perfect_number(input_number):
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")

# 8

# def loading_bar(persantage):
#     number = int(persantage / 10)
#     result = "["
#     for _ in range(number):
#         result += "%"
#     for _ in range(number, 10):
#         result+= "."
#     result += ']'
#     return result
#
#
# def loading_screen(number):
#     if number == 100:
#         print("100% Complete!")
#         print(loading_bar(number))
#     else:
#         result = f"{number}% {loading_bar(number)}"
#         print(result)
#         print("Still loading...")
#
# number = int(input())
# loading_screen(number)

# 9

# def find_factorial(number):
#     result = 1
#     for current_number in range(1, number + 1):
#         result *= current_number
#     return result
#
# number1 = int(input())
# number2 = int(input())
#
# print(f"{find_factorial(number1)/find_factorial(number2):.2f}")

# 10

# def int_array(array):
#     result = []
#     for num in array:
#         result.append(int(num))
#     return result
#
#
# def exchange(array, index):
#     if 0 <= index <= len(array):
#         print("Invalid index")
#         return array
#     else:
#         result = array[index + 1:]
#         result.extend(array[:index + 1])
#         return result
#
#
# def max_odd_even(odd_even):
#
#     if (odd_even == "even" and len(even_list) == 0) or (odd_even == "odd" and len(odd_list)):
#         print("Invalid index")
#         return
#
#     if odd_even == "even":
#         max_elem = even_list[0]
#         for elem in even_list:
#             if elem > max_elem:
#                 max_elem = elem
#     else:
#         max_elem = odd_list[0]
#         for elem in odd_list:
#             if elem > max_elem:
#                 max_elem = elem
#     print(max_elem)
#
#
# def min_odd_even(odd_even):
#     if (odd_even == "even" and len(even_list) == 0) or (odd_even == "odd" and len(odd_list)):
#         print("Invalid index")
#         return
#
#     if odd_even == "even":
#         min_elem = even_list[0]
#         for elem in even_list:
#             if elem < min_elem:
#                 min_elem = elem
#     else:
#         min_elem = odd_list[0]
#         for elem in odd_list:
#             if elem < min_elem:
#                 min_elem = elem
#     print(min_elem)
#
# def first(count, even_odd):
#     result = []
#     if even_odd == "odd":
#         if count > len(odd_list):
#             print("Invalid count")
#             return
#         for index in range(count):
#             result.append(odd_list[index])
#     else:
#         if count > len(even_list):
#             print("Invalid count")
#             return
#         for index in range(count):
#             result.append(even_list[index])
#     return result
#
#
# def last(count, even_odd)
#
#
# array = input().split(" ")
# int_array(array)
# odd_list = []
# even_list = []
#
# for element in array:
#     if element % 2 == 0:
#         even_list.append(element)
#     else:
#         odd_list.append(element)
#
# command = input()
# while command != "end":
#     command_parts = command.split(' ')
#
#     if command_parts[0] == "exchange":
#         array = exchange(array, command_parts[1])
#
#     elif command_parts[0] == "max":
#         max_odd_even(command_parts[1])
#
#     elif command_parts[0] == "min":
#         min_odd_even(command_parts[1])
#
#     elif command_parts[0] == "first":
#         array = first(array, command_parts[1], command_parts[2])
#
#     else:
#         array = last(array, command_parts[1], command_parts[2])
#
#     command = input()




