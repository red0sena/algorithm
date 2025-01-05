from collections import deque

n = int(input())

# chess_list = [[0] * n for _ in range(n)]
queen_count = 0
columns = [0] * n
tl_to_br = [0] * (2*n+1)
tr_to_bl = [0] * (2*n+1)
res = 0


def dfs(i):
    global queen_count, res
    if queen_count == n:
        res += 1
    for j in range(n):
        if columns[j] == 0 and tr_to_bl[i + j] == 0 and tl_to_br[i - j + 1] == 0:
            queen_count += 1
            columns[j] = 1
            tr_to_bl[i + j] = 1
            tl_to_br[i - j + 1] = 1
            dfs(i+1)
            queen_count -= 1
            columns[j] = 0
            tr_to_bl[i + j] = 0
            tl_to_br[i - j + 1] = 0
        else:
            continue

dfs(0)
print(res)