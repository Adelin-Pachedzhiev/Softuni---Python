string = input()
result =[]
[result.extend([int(num) for num in elem.split()]) for elem in reversed(string.split("|"))]
print(result)