from collections import deque


# 1

# numbers = input().split(' ')
# result_stack = []
# while numbers:
#     result_stack.append(numbers.pop())
# print(" ".join(result_stack))

# 2

# command_count = int(input())
# stack = []
# for _ in range(command_count):
#     command_parts = input().split(' ')
#     if command_parts[0] == "1":
#         stack.append(int(command_parts[1]))
#     elif command_parts[0] == "2":
#         if len(stack):
#             stack.pop()
#     elif command_parts[0] == "3":
#         print(max(stack))
#     else:
#         print(min(stack))
# result = f"{stack.pop()}"
# while len(stack):
#     result += f", {stack.pop()}"
#
# print(result)

# 3

# food_available = int(input())
# clients_orders = input().split(' ')
# clients_queue = deque()
#
# for order in clients_orders:
#     clients_queue.appendleft(int(order))
#
# print(max(clients_queue))
#
# while len(clients_queue):
#     next_order = clients_queue.pop()
#     if food_available - next_order >= 0:
#         food_available -= next_order
#     else:
#         clients_queue.append(next_order)
#         break
#
# if len(clients_queue):
#     result_str = 'Orders left:'
#     while len(clients_queue):
#         result_str += f" {clients_queue.pop()}"
#     print(result_str)
# else:
#     print('Orders complete')

# 4

# clothes = [int(elem) for elem in input().split(' ')]
# rack_capacity = int(input())
# current_rack = rack_capacity
# rack_count = 1
#
# while len(clothes):
#     cloth_value = clothes.pop()
#     if current_rack >= cloth_value:
#         current_rack -= cloth_value
#     else:
#         rack_count += 1
#         current_rack = rack_capacity - cloth_value
#
# print(rack_count)

# 6

# {[()]}

# expr = input()
# par_stack = []
# parentheses = {"{": "}", "[": "]", '(': ')'}
# is_correct = True
#
# for char in expr:
#     if char in parentheses.keys():
#         par_stack.append(char)
#     else:
#         last_patentheses = par_stack.pop()
#         if parentheses[last_patentheses] != char:
#             is_correct = False
#             break
#
# if is_correct:
#     print("YES")
# else:
#     print("NO")


