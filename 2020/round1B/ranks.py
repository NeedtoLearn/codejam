def perform_action(R, S, ranks, num_actions, actions):
    if num_actions == (R * (S - 1) + 1) // 2:
        return
    # Now we need to sort ranks in increasing order
    # Every action will perform a swap of 3 piles:
    #   + Pile A: A_start ... A_end cards
    #   + Pile B: B_start ... B_end cards
    #   + Rest: R_start ... R_end cards
    # So each action can create maximum 2 new orderings:
    #   + A_end == R_start
    #   + B_end == A_start
    # A_start always be the first card of the deck
    A_start = 0
    # Now looks for B_end to match with A_start
    found = False
    for i in range(1, R * S):
        # Skip items with same rank as A_start
        if not found and ranks[i] != ranks[A_start]:
            found = True
        # Now look for B_end
        if found and ranks[i] == ranks[A_start]:
            B_end = i
            R_start = i + 1
            break
    # Now look for A_end to perform action
    if R_start < R * S:
        i = B_end - 1
        while i >= 0:
            if ranks[R_start] == ranks[i]:
                A_end = i
                break
            i -= 1
    else:
        # No card in the Rest pile,
        # so Pile A should have same rank.
        A_end = A_start
        while ranks[A_end + 1] == ranks[A_start]:
            A_end += 1
    # Perform action to get new ranks
    print('%d %d' % (A_end - A_start + 1, B_end - A_end))
    actions.append((A_end - A_start + 1, B_end - A_end))
    new_ranks = ranks[A_end+1:B_end+1] + ranks[A_start:A_end+1] + ranks[R_start:]
    perform_action(R, S, new_ranks, num_actions + 1, actions)

T = int(input())
for t in range(1, T + 1):
    R, S = map(int, input().split())
    print('Case #{0}: {1}'.format(t, (R * (S - 1) + 1) // 2))
    # Initial ranks of the deck
    ranks = [r for r in range(1, R + 1)] * S
    actions = []
    perform_action(R, S, ranks, 0, actions)
    verify(actions, R, S)

def verify():
    """ Make sure solution pased all test cases where 2 <= R, S <= 40 """
    for R in range(2, 41):
        for S in range(2, 41):
            # Initial ranks of the deck
            ranks = [r for r in range(1, R + 1)] * S
            sorted_ranks = sorted(ranks)
            # Solve problem and get actions
            actions = []
            perform_action(R, S, ranks, 0, actions)
            # Verify actions
            for A, B in actions:
                ranks = ranks[A:A+B] + ranks[:A] + ranks[A+B:]
            if ranks != sorted_ranks:
                # DEBUG time!!!
                print(R, S, len(actions))
                print(ranks)
                exit()
