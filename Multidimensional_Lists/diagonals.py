rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(rows):
    current_row = [int(x) for x in input().split(', ')]
    matrix.append(current_row)

for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][rows - 1 - i])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")