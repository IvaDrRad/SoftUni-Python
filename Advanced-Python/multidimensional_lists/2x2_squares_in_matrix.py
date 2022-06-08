row, column = [int(x) for x in input().split()]
matrix = []
counter = 0


for _ in range(row):
    matrix.append([el for el in input().split()])

for i in range(row-1):
    for j in range(column-1):
        current_matrix = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            counter += 1

print(counter)