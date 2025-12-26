import sys
import heapq

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

m, n = map(int, input().split()) # m: 가로(열), n: 세로(행)
grid = [list(input().strip()) for _ in range(n)]

# 시작점 찾기
start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'T':
            start_x, start_y = i, j
            grid[i][j] = '0' # 시작점은 다시 방문할 때 0으로 계산하기 위해 변경

# 다익스트라를 위한 거리 배열 (무한대로 초기화)
dist = [[float('inf')] * m for _ in range(n)]

def dijkstra():
    pq = []
    # (소요시간, x, y)
    heapq.heappush(pq, (0, start_x, start_y))
    dist[start_x][start_y] = 0

    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while pq:
        curr_time, x, y = heapq.heappop(pq)

        # 현재 저장된 최단 시간보다 더 오래 걸리는 경우 스킵
        if dist[x][y] < curr_time:
            continue

        # 4방향으로 미끄러지기 시도
        for dx, dy in move:
            nx, ny = x, y
            slide_cost = 0 # 이번 미끄러짐에서 추가되는 시간

            while True:
                nx += dx
                ny += dy

                # 1. 범위를 벗어나면 구멍에 빠진 것과 같으므로 실패 (break)
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                
                cell = grid[nx][ny]

                # 2. 구멍(H)을 만나면 실패 (break)
                if cell == 'H':
                    break
                
                # 3. 바위(R)를 만나면 '직전' 위치에서 멈춤
                elif cell == 'R':
                    bx, by = nx - dx, ny - dy # 바위 전 좌표
                    new_cost = curr_time + slide_cost
                    
                    # 더 적은 시간으로 도달 가능하다면 갱신 및 큐에 추가
                    if dist[bx][by] > new_cost:
                        dist[bx][by] = new_cost
                        heapq.heappush(pq, (new_cost, bx, by))
                    break # 미끄러짐 멈춤
                
                # 4. 출구(E)를 만나면 '현재' 위치에서 멈춤
                elif cell == 'E':
                    new_cost = curr_time + slide_cost
                    if dist[nx][ny] > new_cost:
                        dist[nx][ny] = new_cost
                        heapq.heappush(pq, (new_cost, nx, ny))
                    break # 미끄러짐 멈춤
                
                # 5. 숫자(빙판)인 경우 시간 누적하고 계속 미끄러짐
                else:
                    slide_cost += int(cell)

    # 출구 좌표 찾아서 결과 출력
    result = float('inf')
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'E':
                result = dist[i][j]
    
    return result if result != float('inf') else -1

print(dijkstra())