def make_word(N, L, words):
    words.sort()
    word_set = set(words)
    for i in range(1, L):
        for idx, word in enumerate(words):
            prefix = word[:i]
            for word in words[idx+1:]:
                suffix = word[i:]
                if prefix + suffix not in word_set:
                    return prefix + suffix
    return '-'

def make_word_better(N, L, words):
    for i in range(1, L):
        prefixes = {}
        suffixes = set()
        for word in words:
            prefix = word[:i]
            suffix = word[i:]
            suffixes.add(suffix)
            if prefix not in prefixes:
                prefixes[prefix] = set([suffix])
            else:
                prefixes[prefix].add(suffix)
        for prefix, val in prefixes.items():
            if suffixes - val:
                return prefix + (suffixes - val).pop()
    return '-'

def solve():
    T = int(input())
    for c in range(1, T + 1):
        N, L = map(int, input().split())
        words = [input() for _ in range(N)]
        new_word = make_word_better(N, L, words)
        print('Case #{0}: {1}'.format(c, new_word))

solve()