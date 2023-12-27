from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

de = deque([])

def dfs(depth):
    if depth > m:
        print(' '.join(str(num) for num in de))
        de.pop()
        depth -= 1
        return
    for i in range(1, n+1):
        if de:
           if i < de[-1]:
               continue
        if i in de:
            continue
        de.append(i)
        dfs(depth+1)

    if de:
        de.pop()



dfs(1)