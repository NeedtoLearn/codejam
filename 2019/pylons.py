def is_valid(r1, c1, r2, c2, grid):
    if r1 == r2 or c1 == c2 or r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2 or grid[r2][c2] == 1:
        return False
    return True


def solve(R, C, grid, cell, visited):
    if len(visited) == R * C:
        return visited
    for i in range(R):
        for j in range(C):
            if is_valid(cell[0], cell[1], i, j, grid):
                grid[i][j] = 1
                visited.append((i, j))
                path = solve(R, C, grid, (i, j), visited)
                if path:
                    return path
                grid[i][j] = 0
                visited.pop()
    return None

T = int(input())
for c in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [[0] * C for _ in range(R)]
    grid[0][0] = 1
    path = solve(R, C, grid, (0, 0), [(0, 0)])
    if not path:
        print('Case #{0}: IMPOSSIBLE'.format(c))
    else:
        print('Case #{0}: POSSIBLE'.format(c))
        for cell in path:
            print('%d %d' % (cell[0] + 1, cell[1] + 1))
