from collections import deque

n, m = map(int, input().split(' '))

q = deque()

def dfs():
    if len(q) == m:
        print(' '.join(map(str, q)))
        return

    for i in range(1, n+1):

        if q:
            if q[-1] > i:
                continue

        q.append(i)
        dfs()
        q.pop()

dfs()
