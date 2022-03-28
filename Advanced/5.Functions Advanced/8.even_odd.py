def even_odd(*args):
    command = args[len(args) - 1]
    li = args[:len(args) - 1]

    if command == "even":
        return list(filter(lambda a: a % 2 == 0, li))
    elif command =="odd":
        return list(filter(lambda a: a % 2 != 0, li))

    return command, li

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))