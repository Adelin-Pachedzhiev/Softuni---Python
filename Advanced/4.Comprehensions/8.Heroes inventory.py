heroes = [hero for hero in input().split(", ")]
inventory = {hero:{} for hero in heroes}

while True:
    row_input = input()
    if row_input == "End":
        break

    name, item, cost = row_input.split("-")
    if item not in inventory[name].keys():
        inventory[name][item] = cost

for hero in heroes:
    suma = 0
    for item in inventory[hero].keys():
        suma+= int(inventory[hero][item])
    print(f"{hero} -> Items: {len(inventory[hero].keys())}, Cost: {suma}")

