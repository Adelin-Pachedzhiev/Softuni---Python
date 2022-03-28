# zad 1
# name = input()
# if name == "Johnny":
#     print("Hello, my love!")
# else:
#     print(f"Hello, {name}!")

# zad 2
# age = int(input())
# if age <= 14:
#     print("drink toddy")
# elif age <= 18:
#     print("drink coke")
# elif age <= 21:
#     print("drink beer")
# else:
#     print("drink whisky")

# zad3
# number = int(input())
# if number == 88:
#     print('Leo finally won the Oscar! Leo is happy')
# elif number == 86:
#     print("Not even for Wolf of Wall Street?!")
# elif number < 88:
#     print("When will you give Leo an Oscar?")
# else:
#     print("Leo got one already!")

# zad4
# word = input()
# result = ''
# for char in word :
#     result += char*2
# input(result)

# zad5
# sheep_Num = int(input())
# result = ""
# for number in range(1, sheep_Num + 1):
#     result = result + str(number) + " sheep..."
# print(result)

# zad 6
# year = int(input())
# while true:
#     syear = str(year)
#     if syear[0] != syear[1] and syear[0] != syear[2] and syear[0] != syear[3] and syear[1] != SY

# zad 7

# divisor = int(input())
# bound = int(input())
# num = 0
# result = 0
# while num <= bound:
#     if num % divisor == 0:
#         result = num
#     num += 1
# print(result)

# zzad 8
# str1 = input()
# str2 = input()
# result = ""
# for index in range(0, len(str1)):
#     if str1[index] == str2[index]:
#         continue
#     result = str2[0 : index + 1] + str1[index + 1: len(str1) + 1]
#     print(result)

# zad 9
budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = (1.25 * flour_price) / 4
total_price= flour_price + milk_price + eggs_price
colored_eggs = 0
cozonaks = 0

while budget >= total_price:
    budget -= total_price
    colored_eggs += 3
    cozonaks += 1
    if cozonaks % 3 == 0:
        colored_eggs -= (cozonaks - 2)
print(f"You made {cozonaks} cozonacs! Now you have {colored_eggs} eggs and {format(budget,'0.2f')}BGN left.")

