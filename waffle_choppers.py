def perform_cut(C, V, cols, amount):
    cuts = []
    while len(cuts) < V:
        # Get last cut
        start = cuts[-1] if cuts else 0
        # Find next cut
        found = False
        last_sum = 0
        for c in range(start, C):
            if amount == last_sum + cols[c]:
                cuts.append(c+1)
                found = True
                break
            last_sum += cols[c]
        if not found:
            return []
    return cuts

def sum_grid(waffle, start_row, end_row, start_col, end_col):
    s = 0
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if waffle[r][c] == '@':
                s += 1
    return s

def verify_grids(waffle, R, C, v_cuts, h_cuts, amount):
    for v_idx, v_cut in enumerate(v_cuts):
        for h_idx, h_cut in enumerate(h_cuts):
            start_col = 0 if (v_idx == 0) else v_cuts[v_idx - 1]
            end_col = v_cut
            start_row = 0 if (h_idx == 0) else h_cuts[h_idx - 1]
            end_row = h_cut
            if amount != sum_grid(waffle, start_row, end_row, start_col, end_col):
                return False
    # Verify for last vertical cut
    for h_idx, h_cut in enumerate(h_cuts):
        start_row = 0 if (h_idx == 0) else h_cuts[h_idx - 1]
        end_row = h_cut
        if amount != sum_grid(waffle, start_row, end_row, v_cuts[-1], C):
            return False
    # Verify for last horizontal cut
    for v_idx, v_cut in enumerate(v_cuts):
        start_col = 0 if (v_idx == 0) else v_cuts[v_idx - 1]
        end_col = v_cut
        if amount != sum_grid(waffle, h_cuts[-1], R, start_col, end_col):
            return False
    # Verify bottom right grid
    if amount != sum_grid(waffle, h_cuts[-1], R, v_cuts[-1], C):
            return False
    return True

def cut(R, C, H, V, waffle):
    # Compute total chocolate chips for each row and col
    rows = [waffle[r].count('@') for r in range(R)]
    cols = [0 for c in range(C)]
    for c in range(C):
        for r in range(R):
            if waffle[r][c] == '@':
                cols[c] += 1
    # print(R, C, H, V, waffle)
    # print(cols, rows)
    # Check if possible to divide choc chip into (H+1)x(V+1) grids
    if sum(rows) % ((H+1)*(V+1)) != 0:
        return 'IMPOSSIBLE'
    # Amount choc chips for each vertical cut and horizontal cut
    grid_amount = sum(rows) // ((H+1)*(V+1))
    vertical_amount = sum(rows) // (V+1)
    horizontal_amount = sum(rows) // (H+1)
    # Check if possible for cuts
    vertical_cuts = perform_cut(C, V, cols, vertical_amount)
    horizontal_cuts = perform_cut(R, H, rows, horizontal_amount)
    if len(vertical_cuts) != V or len(horizontal_cuts) != H:
        return 'IMPOSSIBLE'
    # Verify each grid
    if verify_grids(waffle, R, C, vertical_cuts, horizontal_cuts, grid_amount):
        return 'POSSIBLE'
    return 'IMPOSSIBLE'

def solve():
    T = int(input())
    for c in range(1, T + 1):
        R, C, H, V = map(int, input().split())
        waffle = [input() for i in range(R)]
        result = cut(R, C, H, V, waffle)
        print('Case #{0}: {1}'.format(c, result))

solve()