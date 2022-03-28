input_li = [int(num) for num in input().split(", ")]

positive_li = [num for num in input_li if num >= 0]
negative_li = [num for num in input_li if num < 0]
even_li = [num for num in input_li if num % 2 == 0]
odd_li = [num for num in input_li if num % 2 != 0]

print(f"Positive: {', '.join(map(str,positive_li))}")
print(f"Negative: {', '.join(map(str, negative_li))}")
print(f"Even: {', '.join(map(str, even_li))}")
print(f"Odd: {', '.join(map(str, odd_li))}")




