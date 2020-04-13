def get_avg_skill(grid, r, c):
    R, C = len(grid), len(grid[0])
    total_skills = cnt = 0
    for i in range(c - 1, -1, -1):
        if grid[r][i] > 0:
            total_skills += grid[r][i]
            cnt += 1
            break
    for i in range(c + 1, C):
        if grid[r][i] > 0:
            total_skills += grid[r][i]
            cnt += 1
            break
    for i in range(r - 1, -1, -1):
        if grid[i][c] > 0:
            total_skills += grid[i][c]
            cnt += 1
            break
    for i in range(r + 1, R):
        if grid[i][c] > 0:
            total_skills += grid[i][c]
            cnt += 1
            break
    return total_skills / cnt if cnt > 0 else 0

def solve(R, C, grid, prev_sum, acc):
    eliminated = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] > 0 and grid[r][c] < get_avg_skill(grid, r, c):
                eliminated.append((r, c))
    if not eliminated:
        return acc
    for r, c in eliminated:
        prev_sum -= grid[r][c]
        grid[r][c] = -1
    return solve(R, C, grid, prev_sum, acc + prev_sum)

T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    prev_sum = 0
    grid = [[0] * C for _ in range(R)]
    for r in range(R):
        for c, lvl in enumerate(input().split()):
            prev_sum += int(lvl)
            grid[r][c] = int(lvl)
    ans = solve(R, C, grid, prev_sum, prev_sum)
    print('Case #{0}: {1}'.format(t, ans))
