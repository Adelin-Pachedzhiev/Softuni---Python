# # 1
#
# n = int(input())
#
# primary_diagonal_total = 0
# secondary_diagonal_total = 0
# matrix =[]
#
# for _ in range(n):
#     row = [int(num) for num in input().split(" ")]
#     matrix.append(row)
#
# """""
# [
#     [11, 2,  4],
#     [ 4, 5,  6],
#     [10, 8, -12],
#
#
# ]
# """""
# for index in range(n):
#     primary_diagonal_total += matrix[index][index]
#     secondary_diagonal_total += matrix[index][abs(index - n ) - 1]
#
# print(abs(primary_diagonal_total - secondary_diagonal_total))

# 2

# n , m = [int(num) for num in input().split(" ")]
# matrix = []
# equal_count = 0
#
# for _ in range(n):
#     row = input().split(" ")
#     matrix.append(row)
#
#
# for row in range(n - 1):
#     for column in range(m - 1):
#         a1 = matrix[row][column]
#         a2 = matrix[row][column + 1]
#         b1 = matrix[row + 1][column]
#         b2 = matrix[row + 1][column + 1]
#         if a1 == a2 and b1 == b2 and a1 == b1:
#             equal_count += 1
#
# print(equal_count)

# 3

# def check_input(command: str, n, m):
#     commands = command.split(" ")
#     if (len(commands) == 5) and (commands[0] == "swap") and (int(commands[1]) < n) and (int(commands[2]) < m) and \
#             (int(commands[3]) < n) and (int(commands[4]) < m):
#         return True
#     return False
#
#
# n, m = [int(num) for num in input().split(" ")]
# matrix = []
#
# for _ in range(n):
#     row = input().split(" ")
#     matrix.append(row)
#
# while True:
#     command_raw = input()
#     if command_raw == "END":
#         break
#
#     if not check_input(command_raw, n, m):
#         print('Invalid input!')
#         continue
#     else:
#         commands = command_raw.split(" ")
#         row1 = int(commands[1])
#         column1 = int(commands[2])
#         row2 = int(commands[3])
#         column2 = int(commands[4])
#         first_element = matrix[row1][column1]
#         matrix[row1][column1] = matrix[row2][column2]
#         matrix[row2][column2] = first_element
#
#         for i in range(n):
#             print(" ".join([str(elem) for elem in matrix[i]]))


# 4
# from collections import deque
#
# n, m = [int(num) for num in input().split(" ")]
# word = input()
#
# queue = deque(word)
#
# for row_num in range(n):
#     row = ""
#     for _ in range(m):
#         char = queue.popleft()
#         row += char
#         queue.append(char)
#     if row_num % 2 == 1:
#         print(row[::-1])
#     else:
#         print(row)

# 5

# n = int(input())
# matrix = []
# cells_alive_count = 0
# total_sum = 0
#
# for _ in range(n):
#     row = [int(num) for num in input().split(' ')]
#     matrix.append(row)
#
# bombs = [[int(xy) for xy in coord.split(',')] for coord in input().split(" ")]
# for bomb in bombs:
#     row, column = bomb
#     bomb_value = matrix[row][column]
#
#     for cur_row in range(row - 1, row + 2):
#         for cur_column in range(column - 1, column + 2):
#             if cur_row == row and cur_column == column:
#                 matrix[row][column] = 0
#                 continue
#             if cur_row < 0 or cur_row >= n or cur_column < 0 or cur_column >= n:
#                 continue
#             if matrix[cur_row][cur_column] <= 0:
#                 continue
#             matrix[cur_row][cur_column] -= bomb_value
#
# for row in range(n):
#     for column in range(n):
#         if matrix[row][column] > 0:
#             total_sum += matrix[row][column]
#             cells_alive_count += 1
#
# print(f"Alive cells: {cells_alive_count}")
# print(f"Sum: {total_sum}")
#
# for row in range(n):
#     print(" ".join([str(cell) for cell in matrix[row]]))

# 6
# def find_start(matrix):
#     for row in range(field_size):
#         for column in range(field_size):
#             if matrix[row][column] == "s":
#                 return (row, column)
#
#
# def coals_left(matrix):
#     coals_count = 0
#     for row in range(field_size):
#         for column in range(field_size):
#             if matrix[row][column] == "c":
#                 coals_count += 1
#     return coals_count
#
#
# matrix = []
# coal_collected = 0
#
# field_size = int(input())
# commands = [command for command in input().split(" ")]
#
# for _ in range(field_size):
#     row = input().split(" ")
#     matrix.append(row)
#
# curr_row, curr_column = find_start(matrix)
#
# for command in commands:
#
#     if command == "left" and curr_column - 1 >= 0:
#         curr_column -= 1
#     elif command == "right" and curr_column + 1 < field_size:
#         curr_column += 1
#     elif command == "up" and curr_row - 1 >= 0:
#         curr_row -= 1
#     elif command == "down" and curr_row + 1 < field_size:
#         curr_row += 1
#     else:
#         continue
#
#     position_value = matrix[curr_row][curr_column]
#     matrix[curr_row][curr_column] = "*"
#
#     if position_value == "c":
#         coal_collected += 1
#         if not coals_left(matrix):
#             print(f"You collected all coal! ({curr_row}, {curr_column})")
#             break
#     elif position_value == "e":
#         print(f'Game over! ({curr_row}, {curr_column})')
#         break
# else:
#     print(f"{coals_left(matrix)} pieces of coal left. ({curr_row}, {curr_column})")

# 7
def move_bunnies(matrix, rows, columns):
    for curr_row in range(rows):
        for curr_column in range(columns):
            if matrix[curr_row][curr_column] == "B":
                if curr_row - 1 >= 0:
                    matrix[curr_row - 1][curr_column] = "B"
                if curr_row + 1 < rows:
                    matrix[curr_row + 1][curr_column] = "B"
                if curr_column - 1 >= 0:
                    matrix[curr_row][curr_column - 1] = "B"
                if curr_column + 1 < columns:
                    matrix[curr_row][curr_column + 1] = "B"


rows, columns = [int(coord) for coord in input().split(" ")]

pl_row = 0
pl_column = 0

matrix = []
for cur_row in range(rows):
    row = list(input())
    if "P" in row:
        pl_row = cur_row
        pl_column = row.index("P")
    matrix.append(row)

commands = [command for command in input().split()]
for command in commands:
    if command == "L":
        pl_column -= 1
    elif command == "R":
        pl_column += 1
    elif command == "U":
        pl_row -=1
    else:
        pl_row += 1

    if matrix[pl_row][pl_column] == "B":
        print(f"dead: {pl_row} {pl_column}")
        move_bunnies(matrix, rows, columns)
        break
    elif pl_row < 0 or pl_row > rows or pl_column < 0 or pl_column > columns:
        print(f"won: {pl_row} {pl_column}")
        move_bunnies(matrix, rows, columns)
        break
    move_bunnies(matrix, rows, columns)
    if matrix[pl_row][pl_column] == "B":
        print(f"dead: {pl_row} {pl_column}")
        break










