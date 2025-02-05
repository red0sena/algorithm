n, m = map(int, input().split())

input_list = [list(map(int, input().split())) for _ in range(n)]

k = int(input())


prefix = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = (prefix[i-1][j]
                        + prefix[i][j-1]
                        - prefix[i-1][j-1]
                        + input_list[i-1][j-1])

for _ in range(k):
    i, j, x, y = map(int, input().split())

    ans = (prefix[x][y]
           - prefix[x][j - 1]
           - prefix[i - 1][y]
           + prefix[i - 1][j - 1])
    print(ans)