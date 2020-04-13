def get_assignee(assignees, start):
    for assignee, end in assignees.items():
        if start >= end:
            return assignee
    return None


def solve(activities):
    activities.sort()
    assignees = {'C': -1, 'J': -1}
    schedule = [''] * len(activities)
    for start, end, idx in activities:
        assignee = get_assignee(assignees, start)
        if not assignee:
            return 'IMPOSSIBLE'
        schedule[idx] = assignee
        assignees[assignee] = end
    return ''.join(schedule)


T = int(input())
for x in range(1, T + 1):
    N = int(input())
    activities = []
    for i in range(N):
        start, end = map(int, input().split())
        activities.append((start, end, i))
    y = solve(activities)
    print('Case #{0}: {1}'.format(x, y))
