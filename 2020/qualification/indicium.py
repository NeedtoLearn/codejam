def get_natural_diagonal(N, K):
    if N == 2 and K in (2, 4):
        return [K // 2] * 2
    if N == 3 and K in (3, 6):
        return [1, 2, 3] if K == 6 else [1, 1, 1]
    if K == N**2:
        return [N] * N
    if K == N + 1 or K > N * (N - 1) or N in (2, 3):
        return None
    diagonal = [1] * N
    for i in range(N - 2):
        diagonal[i] = min((K - 2) // (N - 2), N)
    if (K - 2) // (N - 2) >= N:
        diagonal[-1] += (K - 2) - N * (N - 2)
    else:
        for i in range((K - 2) % (N - 2)):
            diagonal[i] += 1
    return diagonal

def fill_square(square, rows, cols, r, c):
    N = len(square)
    if r >= N:
        return square
    if r == c:
        if c + 1 < N:
            return fill_square(square, rows, cols, r, c + 1)
        else:
            return fill_square(square, rows, cols, r + 1, 0)
    for i in range(1, N + 1):
        if (rows[r] & (1 << i)) == 0 and (cols[c] & (1 << i)) == 0:
            # Found potential number, update square and data
            square[r][c] = i
            rows[r] |= 1 << i
            cols[c] |= 1 << i
            # Try to move on to next cell
            if c + 1 < N:
                filled_square = fill_square(square, rows, cols, r, c + 1)
            else:
                filled_square = fill_square(square, rows, cols, r + 1, 0)
            if not filled_square:
                # Reverse square state and its data
                square[r][c] = 0
                rows[r] &= ~(1 << i)
                cols[c] &= ~(1 << i)
            else:
                return filled_square
    return None

def get_natural_latin_square(N, K):
    # Try to get natural diagonal
    diagonal = get_natural_diagonal(N, K)
    if not diagonal:
        return None
    # Fill in initial data for backtracking
    rows = [0] * N
    cols = [0] * N
    square = [[0] * N for _ in range(N)]
    for i in range(N):
        square[i][i] = diagonal[i]
        rows[i] |= 1 << diagonal[i]
        cols[i] |= 1 << diagonal[i]
    # Backtracking to fill the empty cells
    return fill_square(square, rows, cols, 0, 0)

def verify_square(N, K, square):
    """ Verify if the square is a natural latin square """
    if not square:
        return
    # Check diagonal
    if K != sum(square[i][i] for i in range(N)):
        raise Exception('Diagonal sum not same as K!\n %s' % square)
    # Check rows
    for i in range(N):
        if len(set(square[i])) < N:
            raise Exception('Not unique row: %s' % square[i])
    # Check cols
    for i in range(N):
        if len(set(square[j][i] for j in range(N))) < N:
            raise Exception('Not unique col: %s' % [square[j][i] for j in range(N)])

# if __name__ == "__main__":
#     n = 50
#     k = 50
#     square = get_natural_latin_square(n, k)
#     verify_square(n, k, square)
