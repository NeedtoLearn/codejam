def cal_remain(votes, N):
    return (votes * 1000 // N) % 10

def cal_per(votes, N):
    """ Calculate percentage of votes over N
        with proper rounding. """
    main = votes * 100 // N
    if cal_remain(votes, N) >= 5:
        return main + 1
    return main

def _sanitize_remain(remain):
    # If remain >= 5 makes it 0 to ignore them because 
    # they don't need more vote to be rounded up. 
    return remain if remain < 5 else 0

def find_max_percentage(N, C):
    voted = sum(C)
    # Check if remain of 1/N is more than 5,
    # If so, make each left over votes for new language.
    if cal_remain(1, N) >= 5:
        return sum(cal_per(c, N) for c in C) + (N - voted) * cal_per(1, N)
    # Consider each left over to see if they should 
    # vote for an existing language or new one. 
    # If it can make percentage of existing language round up, 
    # then vote for that language. Otherwise, vote for new language.
    for _ in range(N - voted):
        # TODO: use heap to improve efficieny from O(N2logN) to O(NlogN)
        # Sort C in non-decreasing order of remain in percentage, 
        # tricky part: if remain >= 5 make it 0 to ignore them 
        # because they don't need more vote to be rounded up. 
        C.sort(key=lambda c: _sanitize_remain(cal_remain(c, N)), reverse=True)
        if C[0] > 0 and cal_remain(C[0], N) + cal_remain(1, N) >= 5:
            C[0] += 1
        else:
            C.append(1)
    return sum(cal_per(c, N) for c in C)

def solve():
    T = int(input())
    for c in range(1, T + 1):
        N, _ = map(int, input().split())
        C = list(map(int, input().split()))
        result = find_max_percentage(N, C)
        print('Case #{0}: {1}'.format(c, result))

solve()