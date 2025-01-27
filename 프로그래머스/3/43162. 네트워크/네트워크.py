count = 0
def solution(n, computers):
    visited = [-1] * n

    def dfs(depth):
        global count
        for j in range(n):
            if depth == j:
                continue
            if computers[depth][j] == 1 and visited[j] == -1:
                visited[j]= 1
                count += 1
                dfs(j)


    for i in range(n):
        visited[i] = 1
        dfs(i)

    if n-count <= 0:
        return 1
    else:
        return n-count

