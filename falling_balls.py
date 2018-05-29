def solve(C, B):
    if B[0] == 0 or B[-1] == 0:
        return -1, 'IMPOSSIBLE'
    cur_col = -1
    layout = [['.'] * C for _ in range(C)]
    for col, cnt in enumerate(B):
        for _ in range(cnt):
            cur_col += 1
            if cur_col < col:
                for k in range(cur_col, col):
                    layout[k-cur_col][k] = '\\'
            elif cur_col > col:
                for k in range(cur_col, col, -1):
                    layout[cur_col-k][k] = '/'
    num_row = 0
    formated_layout = ''
    for row in layout:
        num_row += 1
        formated_layout += '\n' + ''.join(row)
        if row == ['.'] * C:
            return num_row, formated_layout

T = int(input())
for c in range(1, T + 1):
    C = int(input())
    B = list(map(int, input().split()))
    num_row, layout = solve(C, B)
    if num_row > 0:
        print('Case #{0}: {1}{2}'.format(c, num_row, layout))
    else:
        print('Case #{0}: {1}'.format(c, layout))