def list_manipulator(*args):
    list, command, place, *other_params = args

    if command == "add":
        if place == "beginning":
            other_params.extend(list)
            list = other_params
            return list
        elif place == "end":
            list.extend(other_params)
            return list

    elif command == "remove":

        if not other_params:
            other_params = [1]

        if place == "beginning":
            return list[other_params[0]:]

        elif place == "end":
            return list[: (len(list) - other_params[0])]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
