def create_pairs(color, count):
    if color == 'R': pair = 'GR'
    elif color == 'Y': pair = 'VY'
    else: pair = 'OB'
    return pair * count

def replace_color(result, color, count):
    if count > 0:
        pairs = create_pairs(color, count)
        if not result:
            result = pairs
        else:
            result = result.replace(color, color + pairs, 1)

def solve(N, R, O, Y, G, B, V):
    # Check if it's possible for mixed colors to exist
    if O > B or G > R or V > Y or 
            (O == B and B > O and (Y > 0 or R > 0)) or
            (G == R and R > 0 and (Y > 0 or B > 0)) or
            (V == Y and Y > 0 and (R > 0 or B > 0)):
        return 'IMPOSSIBLE'
    # Merge R&G, Y&V, B&O and update R, Y, B 
    # because RGRG...R is equivalent to R.
    # Now, it becomes problem with just 3 main colors: R, Y, B.
    R -= G
    Y -= V
    B -= O
    # Make list of unicorns
    unicorns = [(R, 'R'), (Y, 'Y'), (B, 'B')]
    unicorns.sort(reverse=True)
    # Check if its possible for circular stable just for 3 main colors
    if unicorns[0][0] > unicorns[1][0] + unicorns[2][0]:
        return "IMPOSSIBLE"
    # Get solution for 3 main colors
    stable = [unicorns[0][1] for i in range(unicorns[0][0])]
    for i in range(unicorns[1][0] + unicorns[2][0]):
        if i < unicorns[1][0]:
            stable[i % unicorns[0][0]] += unicorns[1][1]
        else:
            stable[i % unicorns[0][0]] += unicorns[2][1]
    result = ''.join(stable)
    # Replace a single color with a group if mixed color exists
    replace_color(result, 'R', G)
    replace_color(result, 'Y', V)
    replace_color(result, 'B', O)
    return result

if __name__ == "__main__":
    inputs = open('stable_neighbors.input.txt')
    outputs = open('stable_neighbors.output.txt')
    T = int(inputs.readline())
    for c in range(1, T + 1):
        N, R, O, Y, G, B, V = map(int, inputs.readline().split())
        result = solve(N, R, O, Y, G, B, V)
        outputs.write('Case #{0}: {1}\n'.format(c, result))
    inputs.close()
    outputs.close()