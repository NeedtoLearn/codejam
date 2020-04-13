from collections import defaultdict

def solve(words, idx):
    count, num_singles = 0, 0
    # Group the words based on current idx
    groups = defaultdict(list)
    for word in words:
        if len(word) <= idx:
            num_singles += 1
        else:
            groups[word[idx]].append(word)
    # Filter out the single ones, and continue with other groups
    for group in groups.values():
        if len(group) > 1:
            matched, single = solve(group, idx + 1)
            count += matched
            num_singles += single
        else:
            num_singles += 1
    # Compute pairs from singles
    count += min(idx * 2, num_singles - (num_singles % 2))
    return count, num_singles % 2

T = int(input())
for c in range(1, T + 1):
    N = int(input())
    words = [input()[::-1] for _ in range(N)]
    ans, _ = solve(words, 0)
    print('Case #{0}: {1}'.format(c, ans))
