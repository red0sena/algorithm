import sys


N = int(sys.stdin.readline())

map = []
for _ in range(N):
    map.append(sys.stdin.readline().strip())


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(i, j, count):
    for direction in range(4):
        newdx = i + dx[direction]
        newdy = j + dy[direction]
        if 0 <= newdx < N and 0 <= newdy < N:
            if map[newdx][newdy] == '0' or visited[newdx][newdy] == 1:
                continue
            else:
                if map[newdx][newdy] == '1' and visited[newdx][newdy] == 0:
                    visited[newdx][newdy] = 1
                    count += 1
                    count = dfs(newdx, newdy, count)
    
    return count
            
    

visited = [[0 for j in range(N)] for i in range(N)]


count_list = []
for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and visited[i][j] == 0:
            visited[i][j] = 1
            count = dfs(i, j, 1)
            count_list.append(count)

print(len(count_list))
count_list.sort()
for count in count_list:
    print(count)

