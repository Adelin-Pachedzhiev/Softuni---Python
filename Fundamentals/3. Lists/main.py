# 1
# str = input()
#
# lst = str.split(" ")
# for index in range(len(lst)):
#     lst[index] = -int(lst[index])
# print(lst)

# 2
# factor = int(input())
# count = int(input())
#
# result = []
# index = 1
# while len(result) < count:
#     if index % factor == 0:
#         result.append(index)
#     index+=1
# print(result)

# 3
# log = input().split(" ")
# a = list(range(11))
# b = list(range(11))
# is_terminated = False
# for card in log:
#
#     team, player = card.split('-')
#     player = int(player)
#     if team == "A":
#         if player in a:
#             a.remove(player)
#     else:
#         if player in b:
#             b.remove(player)
#     if len(a) < 7 or len(b) < 7:
#         is_terminated = True
#         break
# print(f"Team A - {len(a)}; Team B - {len(b)}")
# if is_terminated:
#     print("Game was terminated")

# 4
# numbers = input().split(', ')
# beggars_count = int(input())
# beggar_earnings = []
# is_done = False
# results = []
#
# for _ in range(beggars_count):
#     beggar_earnings.append([])
#
# while len(numbers) > 0 and not is_done:
#     for beggar in range(beggars_count):
#         beggar_earnings[beggar].append(int(numbers[0]))
#         numbers.remove(numbers[0])
#         if len(numbers) <= 0:
#             is_done = True
#             break
#
# for beggar in beggar_earnings:
#     sum = 0
#     for numbers in beggar:
#         sum += numbers
#     results.append(sum)
#
# print(results)

# 5
# cards = input().split(' ')
# shiffles_num = int(input())
#
# for _ in range(shiffles_num):
#     current_deck = []
#     for index in range(int(len(cards)/2)):
#         current_deck.append(cards[index])
#         current_deck.append(cards[index + int(len(cards)/2)])
#     cards = current_deck
# print(cards )

# 6
# numbers = input().split()
# n_remove = int(input())
#
# for index in range(len(numbers)):
#     numbers[index] = int(numbers[index])
#
# for _ in range(n_remove):
#     min_number = numbers[0]
#     for num in numbers:
#         if num < min_number:
#             min_number = num
#     numbers.remove(min_number)
#
# for index in range(len(numbers)):
#     numbers[index] = str(numbers[index])
# print(', '.join(numbers))

# 7

# gifts = input().split(" ")
# command = input()
# while command != "No Money":
#     if "OutOfStock" in command:
#         for index in range(len(gifts)):
#             gift_name = command.split(" ")[1]
#             if gifts[index] == gift_name:
#                 gifts[index] = None
#     elif "Required" in command:
#         command_name, gift_name, index = command.split()
#         index = int(index)
#         if len(gifts) > index:
#             gifts[index] = gift_name
#     elif "JustInCase" in command:
#         gift_name = command.split(" ")[1]
#         gifts[len(gifts) - 1] = gift_name
#     command = input()
# for elem in gifts:
#     if elem != None:
#         print(elem, end=" ")

# 8

# fires = input().split("#")
# water = int(input())
# cells = []
# total_fire = 0
# efford = 0
# for fire in fires:
#     type_of_fire, value_of_cell = fire.split(' = ')
#     value_of_cell = int(value_of_cell)
#     if not ((type_of_fire == "Low" and 1 <= value_of_cell <= 50) or (type_of_fire == "Medium" and 51 <= value_of_cell <= 80) or (type_of_fire == "High" and 81 <= value_of_cell <=125)):
#         continue
#     if water - value_of_cell > 0:
#         water -= value_of_cell
#         efford += 0.25*value_of_cell
#         cells.append(value_of_cell)
#         total_fire += value_of_cell
#
# print("Cells:")
# for cell in cells :
#     print(f" - {cell}")
# print(f"Effort: {efford:.2f}")
# print(f"Total Fire: {total_fire}")

# 9
# collection = input().split("|")
# budget = int(input())
# products = []
# spend_money = 0
# earned_money = 0
# for index in range(len(collection)):
#     product_type, product_price = collection[index].split("->")
#     product_price = float(product_price)
#     if (product_type == "Clothes" and product_price <= 50) or (product_type == "Shoes" and product_price <= 35) or (
#             product_type == "Accessories" and product_price <= 20.5):
#         if budget - product_price >= 0:
#             budget -= product_price
#             spend_money += product_price
#             products.append(product_price * 1.4)
#
# for product in products:
#     print(f"{product:.2f}", end=" ")
#     earned_money += product
# print()
# print(f"Profit: {(earned_money - spend_money):.2f}")
#
# if (earned_money + budget) >= 150:
#     print("Hello, France!")
# else:
#     print("Time to go.")

# 10

