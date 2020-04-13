def should_eliminate(r, c, grid, compass_neighbors):
    # Skip dummy cells and alr eliminated cells
    if grid[r][c] == 0:
        return False
    # Only consider valid dancers - ignore dummy cells
    neighbors = [(i, j) for i, j in compass_neighbors[r][c] if grid[i][j] > 0]
    return len(neighbors) * grid[r][c] < sum(grid[i][j] for i, j in neighbors)

def update_neighbors(r, c, compass_neighbors):
    r_left, c_left = compass_neighbors[r][c][0]
    compass_neighbors[r_left][c_left][1] = compass_neighbors[r][c][1]
    r_right, c_right = compass_neighbors[r][c][1]
    compass_neighbors[r_right][c_right][0] = compass_neighbors[r][c][0]
    r_up, c_up = compass_neighbors[r][c][2]
    compass_neighbors[r_up][c_up][3] = compass_neighbors[r][c][3]
    r_down, c_down = compass_neighbors[r][c][3]
    compass_neighbors[r_down][c_down][2] = compass_neighbors[r][c][2]

def solve(
        grid, compass_neighbors, prev_eliminated,
        prev_interest_lvl, total_interest_lvl,
        is_first_round=False):
    eliminated = set()
    if is_first_round:
        # Check every dancer for elimination in first round
        for r in range(R):
            for c in range(C):
                if should_eliminate(r, c, grid, compass_neighbors):
                    eliminated.add((r,c))
    else:
        # Only check dancers which are compass neighbors of
        # prev eliminated dancer in sub-sequence rounds
        for r, c in prev_eliminated:
            for i, j in compass_neighbors[r][c]:
                if should_eliminate(i, j, grid, compass_neighbors):
                    eliminated.add((i, j))
    # Update compass neighbors of eliminated cells
    for r, c in eliminated:
        prev_interest_lvl -= grid[r][c]
        update_neighbors(r, c, compass_neighbors)
        grid[r][c] = 0
    # Stop competition if no one is eliminated
    if not eliminated:
        return total_interest_lvl
    return solve(
        grid, compass_neighbors, eliminated,
        prev_interest_lvl, total_interest_lvl + prev_interest_lvl
    )

T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    cur_interest_lvl = 0
    grid = [[0] * (C + 1) for _ in range(R + 1)]
    compass_neighbors = [
        [[(R, C)] * 4 for i in range(C + 1)] for j in range(R + 1)
    ]
    for r in range(R):
        for c, lvl in enumerate(input().split()):
            cur_interest_lvl += int(lvl)
            grid[r][c] = int(lvl)
            compass_neighbors[r][c] = [
                (r, c - 1) if c > 0 else (R, C),
                (r, c + 1) if c < C - 1 else (R, C),
                (r - 1, c) if r > 0 else (R, C),
                (r + 1, c) if r < R - 1 else (R, C)
            ]
    ans = solve(
        grid, compass_neighbors, set(), cur_interest_lvl,
        cur_interest_lvl, is_first_round=True
    )
    print('Case #{0}: {1}'.format(t, ans))
