rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []
total_sum = 0

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for index in range(rows):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][rows - 1 - index])

total_sum = abs((sum(primary_diagonal)) - (sum(secondary_diagonal)))
print(total_sum)