def solve(robots):
    moves = []
    for i in range(500):
        other_moves = {robot[i % len(robot)] for robot in robots}
        if len(other_moves) == 3:
            return 'IMPOSSIBLE'
        if len(other_moves) == 1:
            if 'R' in other_moves:
                move = 'P'
                loser_move = 'R'
            elif 'P' in other_moves:
                move = 'S'
                loser_move = 'P'
            else:
                move = 'R'
                loser_move = 'S'
        else:
            if 'R' in other_moves:
                if 'P' in other_moves:
                    move = 'P'
                    loser_move = 'R'
                else:
                    move = 'R'
                    loser_move = 'S'
            else:
                move = 'S'
                loser_move = 'P'
        moves.append(move)
        robots = {robot for robot in robots if robot[i % len(robot)] != loser_move}
        if not robots:
            return ''.join(moves)
    return 'IMPOSSIBLE'

T = int(input())
for c in range(1, T + 1):
    A = int(input())
    robots = {input() for _ in range(A)}
    ans = solve(robots)
    print('Case #{0}: {1}'.format(c, ans))