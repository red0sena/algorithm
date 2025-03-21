import sys
input = sys.stdin.readline

n, m = map(int, input().split())

input_list = [list(map(int, input().split())) for _ in range(n)]

prefix = [[0] * (m+1) for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] + input_list[i-1][j-1] - prefix[i-1][j-1]


k = int(input())

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    ans = (
        prefix[x2][y2]
        - prefix[x2][y1-1]
        - prefix[x1-1][y2]
        + prefix[x1-1][y1-1]
    )
    print(ans)



