def calculate_total_attacks(P):
    damage = 1
    total_attacks = 0
    for c in P:
        if c == 'C':
            damage *= 2
        else:
            total_attacks += damage
    return total_attacks

def hack_v2(D, P):
    """ Find the right most 'CS' and swap util D >= total_attacks """
    num_hacks = 0
    while True:
        # Check if the shield can survive attacks
        if D >= calculate_total_attacks(P):
            return num_hacks
        # Find right most CS
        idx = P.rfind('CS')
        # There is no more CS to swap, shield can't survive
        if idx == -1:
            return 'IMPOSSIBLE'
        # Perform swap
        num_hacks += 1
        P = P[:idx] + 'SC' + P[idx+2:]

def hack(D, P):
    """ Similar to buble sort (move C towards the end) """
    # Find positions of charge instructions and intial attacks
    C_positions = []
    total_attacks = 0
    for idx, c in enumerate(P):
        if c == 'C':
            C_positions.append(idx)
        else:
            total_attacks += pow(2, len(C_positions))
    # Check if shield already withstand the attacks
    if D >= total_attacks:
        return 0
    # Slowly move each charge instruction towards the end
    N = len(P)
    num_hacks = 0
    for idx, pos in enumerate(reversed(C_positions)):
        # Move each C towards the end
        for _ in range(pos + 1, N - idx):
            # Recalculate total attack after each swap
            num_hacks += 1
            total_attacks -= pow(2, len(C_positions) - 1 - idx)
            if D >= total_attacks:
                return num_hacks
    return 'IMPOSSIBLE'

def solve():
    T = int(input())
    for c in range(1, T + 1):
        D, P = input().split()
        num_hacks = hack_v2(int(D), P)
        print('Case #{0}: {1}'.format(c, num_hacks))

solve()