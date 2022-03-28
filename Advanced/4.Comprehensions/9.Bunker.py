categories_li = [elem for elem in input().split(", ")]

items = {category: {} for category in categories_li}

n = int(input("enter n"))

for _ in range(n):
    category, item, raw_specs = input().split(" - ")
    quantity, quality = raw_specs.split(";")
    quality = int(quality[quality.index(":") + 1 : len(quality)])
    quantity = int(quantity[quantity.index(":") + 1 : len(quantity)])

    if item not in items[category].keys():
        items[category][item] = {}
    items[category][item]["quantity"] = quantity
    items[category][item]["quality"] = quality

sum_quantity = 0
sum_quality = 0
for category in categories_li:
    for item in items[category].keys():
        sum_quantity += items[category][item]["quantity"]
        sum_quality += items[category][item]["quality"]

print(f"Count of items: {sum_quantity}")
print(f"Average quality: {sum_quality/len(categories_li):.2f}")

for category in categories_li:
    print(f"{category} -> {', '.join(items[category].keys())}")