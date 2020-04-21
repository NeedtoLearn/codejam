import sys

# Try to throw dart at crucial points to get first point in the circle
# Crucial points are: (0, 0), (10**9 // 2, 10**9 // 2), (10**9 // 2, -10**9 // 2),
#                       (-10**9 // 2, -10**9 // 2), (-10**9 // 2, 10**9 // 2)
# Regardless of radius (>= 10**9 // 2), one of the above points must be in the circle.
crucial_points = (
    (0, 0), (10**9 // 2, 10**9 // 2), (10**9 // 2, -10**9 // 2),
    (-10**9 // 2, -10**9 // 2), (-10**9 // 2, 10**9 // 2)
)

# Flag to determine if we accidentally hit center while looking to arcs
found_center = False

def throw_dart(x, y):
    print(x, y)
    sys.stdout.flush()
    return input()

def find_point_in_circle():
    global found_center
    for x, y in crucial_points:
        result = throw_dart(x, y)
        if result != 'MISS':
            found_center = (result == 'CENTER')
            return x, y

def search_horizontal_intersection(x_from, x_to, y, is_circle_on_left=False):
    global found_center
    if x_from >= x_to:
        return x_from
    # Need this to prevent being stuck in infinite loop!!!
    if is_circle_on_left:
        mid = (x_from + x_to + 1) // 2
    else:
        mid = (x_from + x_to - 1) // 2
    result = throw_dart(mid, y)
    if result == 'MISS':
        if is_circle_on_left:
            return search_horizontal_intersection(x_from, mid-1, y, is_circle_on_left)
        else:
            return search_horizontal_intersection(mid+1, x_to, y, is_circle_on_left)
    elif result == 'HIT':
        if is_circle_on_left:
            return search_horizontal_intersection(mid, x_to, y, is_circle_on_left)
        else:
            return search_horizontal_intersection(x_from, mid, y, is_circle_on_left)
    else:
        found_center = True
        return -1

def search_vertical_intersection(y_from, y_to, x, is_circle_above=False):
    global found_center
    if y_from >= y_to:
        return y_from
    if is_circle_above:
        mid = (y_from + y_to - 1) // 2
    else:
        mid = (y_from + y_to + 1) // 2
    result = throw_dart(x, mid)
    if result == 'MISS':
        if is_circle_above:
            return search_vertical_intersection(mid+1, y_to, x, is_circle_above)
        else:
            return search_vertical_intersection(y_from, mid-1, x, is_circle_above)
    elif result == 'HIT':
        if is_circle_above:
            return search_vertical_intersection(y_from, mid, x, is_circle_above)
        else:
            return search_vertical_intersection(mid, y_to, x, is_circle_above)
    else:
        found_center = True
        return -1

def  solve():
    x, y = find_point_in_circle()
    if found_center:
        return
    # Try to draw a horizontal line through (x, y) and
    # get two points interect with the circle.
    x_left = search_horizontal_intersection(-10**9, x, y, is_circle_on_left=False)
    if found_center:
        return
    x_right = search_horizontal_intersection(x, 10**9, y, is_circle_on_left=True)
    if found_center:
        return
    # Draw verital line through middle of horizontal line, and
    # the center of the circle is on the middle of the vertical line.
    mid = (x_left + x_right) // 2
    y_above = search_vertical_intersection(y, 10**9, mid, is_circle_above=False)
    if found_center:
        return
    y_below = search_vertical_intersection(-10**9, y, mid, is_circle_above=True)
    if found_center:
        return
    x_center = mid
    y_center = (y_below + y_above) // 2
    result = throw_dart(x_center, y_center)
    if result != 'CENTER':
        exit()

T, A, B = map(int, input().split())
for t in range(1, T + 1):
    solve()
