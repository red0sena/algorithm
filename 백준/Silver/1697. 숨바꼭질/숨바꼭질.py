from collections import deque

n, k = map(int, input().split())


q = deque([(n, 0)])
visited = set()
visited.add(n)

while q:
    v, count = q.popleft()
    if v == k:
        print(count)
        break
    if v * 2 not in visited and v < k:
        visited.add(v * 2)
        q.append((v * 2, count+1))

    if v+1 not in visited and v < k:
        visited.add(v+1)
        q.append((v+1, count+1))

    if v-1 not in visited:
        visited.add(v-1)
        q.append((v-1, count+1))


