input_li = [int(el) for el in input().split(' ')]
new_li = filter(lambda a: a % 2 ==0, input_li)
print(list(new_li))