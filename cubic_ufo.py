import math

def rotate(A):
    # Check for special case
    if A == 1.0:
        return [(0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5)]
    # Only solve test set 1 because only rotate 2 surfaces 
    # of cube, the new surface area is cos0 + sin0 = A.
    cos0 = (A + math.sqrt(2 - A*A)) / 2
    # The new coords for two rotated surfaces
    coord1 = (0.5 * cos0, 0.5 * (A - cos0), 0)
    coord2 = (-0.5 * (A - cos0), 0.5 * cos0, 0)
    # Because we only rotate 2 surfaces, 
    # the 3rd surface still has same coord
    coord3 = (0, 0, 0.5)
    return [coord1, coord2, coord3]

def solve():
    T = int(input())
    for c in range(1, T + 1):
        A = float(input())
        print('Case #{0}:'.format(c))
        coords = rotate(A)
        for coord in coords:
            print(coord[0], coord[1], coord[2])

solve()