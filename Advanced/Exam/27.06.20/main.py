def is_bag_full(bomb_quality):
    for bomb_name in bomb_quality.keys():
        if bomb_quality[bomb_name] < 3:
            return False
    return True


BOMB_TYPES = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}

bomb_quality = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

bomb_effects = [int(effect) for effect in input().split(", ")]
bomb_casings = [int(casing) for casing in input().split(", ")]

while (bomb_effects and bomb_casings) and not is_bag_full(bomb_quality):
    effect = bomb_effects[0]
    while bomb_casings[len(bomb_casings) - 1] >= 0:
        casing = bomb_casings[len(bomb_casings) - 1]
        suma = casing + effect

        if suma in BOMB_TYPES.values():
            for bomb_name in BOMB_TYPES.keys():
                if BOMB_TYPES[bomb_name] == suma:
                    bomb_quality[bomb_name] += 1
                    break
            del bomb_effects[0]
            del bomb_casings[len(bomb_casings) - 1]
            break

        else:
            bomb_casings[len(bomb_casings) - 1] -= 5
            if bomb_casings[len(bomb_casings) - 1] < 0:
                del bomb_casings[len(bomb_casings) - 1]
                break
print("Bene! You have successfully filled the bomb pouch!"
      if is_bag_full(bomb_quality) else
      "You don't have enough materials to fill the bomb pouch."
      )

print("Bomb Effects: "
      + (", ".join([str(effect) for effect in bomb_effects]) if bomb_effects else "empty"))

print("Bomb Casings: "
      + (", ".join([str(casing) for casing in bomb_casings]) if bomb_casings else "empty"))

for bomb in sorted(bomb_quality.keys()):
    print(f"{bomb}: {bomb_quality[bomb]}")




