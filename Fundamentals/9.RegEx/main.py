# 1

# import re
#
# text = input()
# regex =r"\d+"
# result = ""
# while text:
#     result = re.findall(regex, text)
#     for match in result:
#         print(match, end= " ")
#     text = input()

# 2

# import re
# text = input()
# regex = r"(?<=_)\w+"
# #
# # print(",".join(re.findall(regex, text)))

# 3
#
# import re
# text = input()
# search_word = input()
# regex = rf"\b{search_word}\b"
#
# print(len(re.findall(regex, text, re.IGNORECASE)))

# 4
# import re
# text = input()
# regex = r"\b[a-zA-z1-9]+[\.-_]?[a-zA-z1-9]+@[a-zA-z-.]+\b"
#
# print("\n".join(re.findall(regex, text)))

# 5
# import re
# products = []
# regex = r">>(\w+)<<(\d+\.?\d*)!(\d+)"
# total_money = 0
# while True:
#     command = input()
#     if command == "Purchase":
#         break
#
#     found_stuff = re.findall(regex, command)
#     if found_stuff:
#         furniture_name, furniture_price, furniture_quality = found_stuff[0]
#         products.append(furniture_name)
#         total_money += float(furniture_price) * int(furniture_quality)
#
# print(f'Bought furniture:')
# for product in products:
#     print(product)
# print(f'Total money spend: {total_money:.2f}')

# 6
import re
regex = r"www.[a-zA-Z0-9-]+(\.[a-z]+)+"
text = input()

while text:
    found_stuff = re.search(regex, text)
    if found_stuff:
        print(found_stuff[0])
    text = input()

