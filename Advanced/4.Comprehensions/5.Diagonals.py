n = int(input("enter n"))

li = [
    [int(num) for num in input().split(", ")]
    for col in range(n)
]
first_diag = []
second_diag = []

for i in range(n):
    first_diag.append(li[i][i])
    second_diag.append(li[i][n -   1 - i])

print(f"First diagonal: {', '.join(map(str,first_diag))}. Sum: {sum(first_diag)}")
print(f"Second diagonal: {', '.join(map(str,second_diag))}. Sum: {sum(second_diag)}")