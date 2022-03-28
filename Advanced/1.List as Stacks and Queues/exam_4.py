from collections import deque

cups_capacity = deque([int(capacity) for capacity in input().split(" ")])
bottles = deque([int(capacity) for capacity in input().split(" ")])
wasted_water = 0

while len(cups_capacity):
    if not bottles:
        break
    else:
        current_bottle_water = bottles.pop()
        current_cup_capacity = cups_capacity.popleft()

        if current_cup_capacity > current_bottle_water:
            current_cup_capacity -= current_bottle_water
            cups_capacity.appendleft(current_cup_capacity)
        else:
            wasted_water += current_bottle_water - current_cup_capacity

if bottles:
    result = "Bottles:"
    for _ in range(len(bottles)):
        result += f" {bottles.pop()}"
else:
    result = "Cups:"
    for _ in range(len(cups_capacity)):
        result += f" {cups_capacity.popleft()}"
print(result)
print(f"Wasted litters of water: {wasted_water}")
