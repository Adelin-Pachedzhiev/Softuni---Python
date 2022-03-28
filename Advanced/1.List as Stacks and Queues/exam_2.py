from collections import deque


green_light_time = int(input())
orange_light_time = int(input())

cars_to_pass = deque()
cars_passed = 0
while True:

    command = input()
    if command == "END":
        break

    if command =="green":
        green_left = green_light_time
        yellow_left = orange_light_time
        current_car = ""
        car = ""
        # breakpoint()
        while len(cars_to_pass):

            if green_left:
                current_car = cars_to_pass.pop()
                car = current_car

                if green_left > len(current_car):
                    green_left -= len(current_car)
                    cars_passed += 1
                    continue
                else:
                    current_car = current_car[green_left:]
                    green_left = 0
            if yellow_left and current_car:
                if yellow_left < len(current_car):
                    end_char = current_car[yellow_left]
                    print("A crash happened!")
                    print(f"{car} was hit at {end_char}.")
                    exit()
                else:
                    cars_passed += 1

            if green_left == 0:
                break
    else:
        car_brand = command
        cars_to_pass.appendleft(car_brand)


print("Everyone is safe.")
print(f"{cars_passed} total cars passed the crossroads.")


# 10
# 5
# Mercedes
# green
# Mercedes
# BMW
# Skoda
# green
# END