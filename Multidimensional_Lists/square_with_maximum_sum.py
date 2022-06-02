import sys
from sys import maxsize

rows, columns = [int(x) for x in input().split(', ')]
matrix = []
current_sum = 0
max_sum = -sys.maxsize
combination = []

for _ in range(rows):
    current_row = [int(x) for x in input().split(', ')]
    matrix.append(current_row)

for i in range(rows - 1):
    for j in range(columns - 1):
        sub_matrix = matrix[i][j] + matrix[i+1][j] + matrix[i][j+1] + matrix[i+1][j+1]
        if sub_matrix > max_sum:
            combination = []
            max_sum = sub_matrix
            combination.append([matrix[i][j], matrix[i][j+1]])
            combination.append([matrix[i+1][j], matrix[i+1][j+1]])

for el in combination:
    print(*el)
print(max_sum)
