def get_snake_pos(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "S":
                return [i, j]


def find_other_burrow(matrix, first_bur_pos):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == first_bur_pos[0] and j == first_bur_pos[1]:
                continue
            if matrix[i][j] == "B":
                return [i, j]


food_eaten = 0
game_over = False

matrix_size = int(input())
matrix = [[row for row in input()] for column in range(matrix_size)]
snake_pos = get_snake_pos(matrix)

while (food_eaten < 10) and not game_over:
    command = input()
    matrix[snake_pos[0]][snake_pos[1]] = "."
    if command == "up":
        snake_pos[0] -= 1
    elif command == "down":
        snake_pos[0] += 1
    elif command == "left":
        snake_pos[1] -= 1
    else:
        snake_pos[1] += 1
    if not ((0 <= snake_pos[0] < matrix_size) and (0 <= snake_pos[1] < matrix_size)):
        game_over = True
        break
    else:
        if matrix[snake_pos[0]][snake_pos[1]] == "*":
            food_eaten += 1
        elif matrix[snake_pos[0]][snake_pos[1]] == "B":
            matrix[snake_pos[0]][snake_pos[1]] = "."
            snake_pos = find_other_burrow(matrix, snake_pos)
        matrix[snake_pos[0]][snake_pos[1]] = "S"

print("Game over!" if game_over else "You won! You fed the snake.")
print(f"Food eaten: {food_eaten}")
for row in matrix:
    print("".join(row))

