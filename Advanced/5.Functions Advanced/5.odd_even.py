command = input()
input_li = [int(n) for n in input().split(' ')]

if command == "Odd":

    print(len(input_li) *sum(filter(lambda a: a%2 != 0, input_li)))
elif command == "Even":
    print(len(input_li) *sum(filter(lambda a: a%2 == 0, input_li)))
