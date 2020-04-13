from random import randint

output_file = 'test_case.txt'

R = 100
C = 1000

grid = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        grid[i][j] = str(randint(1, 10**6))

with open(output_file, 'w') as fobj:
    for row in grid:
        fobj.write(' '.join(row) + '\n')

