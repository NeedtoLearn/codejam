import sys
from collections import defaultdict

def solve(F):
    # Look for first missing letter
    first_pos = defaultdict(list)
    for i in range(1, 596, 5):
        print(i)
        sys.stdout.flush()
        letter = input()
        first_pos[letter].append(i)
    for letter, pos in first_pos.items():
        if len(pos) < 24:
            first_letter = letter
    # Look for second missing letter
    second_pos = defaultdict(list)
    for pos in first_pos[first_letter]:
        print(pos + 1)
        sys.stdout.flush()
        letter = input()
        second_pos[letter].append(pos + 1)
    for letter, pos in second_pos.items():
        if len(pos) < 6:
            second_letter = letter
    # Look for third missing letter
    third_pos = defaultdict(list)
    for pos in second_pos[second_letter]:
        print(pos + 1)
        sys.stdout.flush()
        letter = input()
        third_pos[letter].append(pos + 1)
    for letter, pos in third_pos.items():
        if len(pos) < 2:
            third_letter = letter
    # Look for last two missing letters
    fourth_letter, fifth_letter = {'A', 'B', 'C', 'D', 'E'} - {first_letter, second_letter, third_letter}
    print(third_pos[third_letter][0] + 1)
    sys.stdout.flush()
    letter = input()
    if letter == fourth_letter:
        print(first_letter + second_letter + third_letter + fifth_letter + fourth_letter)
    else:
        print(first_letter + second_letter + third_letter + fourth_letter + fifth_letter)
    sys.stdout.flush()
    verdict = input()
    if verdict == 'N':
        exit()

T, F = map(int, input().split())
for _ in range(T):
    solve(F)
