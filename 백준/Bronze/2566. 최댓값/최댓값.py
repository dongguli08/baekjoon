matrix = [list(map(int, input().split())) for _ in range(9)]

max_value = -1
max_x, max_y = 0, 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_x, max_y = i, j

print(max_value)
print(max_x + 1, max_y + 1)  # 1-based index 출력
