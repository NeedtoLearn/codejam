def find_error(N, V):
    # Divide V into even and odd indexes list, and sort them
    even = []
    odd = []
    for i in range(N):
        if i % 2 == 0:
            even.append(V[i])
        else:
            odd.append(V[i])
    even.sort()
    odd.sort()
    # Merge even and odd indexes list and look for error
    for i in range(N):
        if i % 2 == 0:
            V[i] = even[i//2] 
        else:
            V[i] = odd[i//2]
        if i > 0 and V[i] < V[i -1]:
            return i - 1
    return 'OK'

def solve():
    T = int(input())
    for c in range(1, T + 1):
        N = int(input())
        V = list(map(int, input().split()))
        print('Case #{0}: {1}'.format(c, find_error(N, V)))

solve()