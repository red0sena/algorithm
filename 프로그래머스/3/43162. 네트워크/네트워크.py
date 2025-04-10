
def solution(n, computers):
    visited = [False] * n


    def dfs(node):
        network = computers[node]
        for i in range(n):
            if network[i] == 1:
                if not visited[i]:
                    visited[i] = True
                    dfs(i)

    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            visited[i] = True
            dfs(i)


    return count