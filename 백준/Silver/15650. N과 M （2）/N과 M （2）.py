n, m = map(int, input().split(' '))
s = []
visited = [False] * (n + 1) # 번호가 1번부터니까 그거 index그대로 사용하려고 1더함



def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        if len(s) >= 1:
            if s[-1] >= i:
                continue
        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False


dfs()
