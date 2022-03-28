r = int(input("enter rows"))
c = int(input("enter columns"))

li = [
    [
        chr(97 + row) + chr(97 + col + row) + chr(97 + row)
        for col in range(c)
    ]
    for row in range(r)
]

for row in li:
    print(" ".join(row))