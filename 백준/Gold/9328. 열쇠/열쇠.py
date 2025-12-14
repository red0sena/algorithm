import sys
from collections import deque

# 빠른 입출력을 위해 설정
input = sys.stdin.readline

# 상하좌우 이동을 위한 방향 벡터
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solve():
    # h: 높이, w: 너비
    h, w = map(int, input().split())
    
    # 지도 입력 (패딩 추가: 상하좌우를 '.'로 감쌈)
    grid = ['.' * (w + 2)]
    for _ in range(h):
        grid.append('.' + input().strip() + '.')
    grid.append('.' * (w + 2))
    
    # 초기 열쇠 정보 입력
    keys_input = input().strip()
    keys = [False] * 26  # a-z 열쇠 보유 여부
    
    if keys_input != '0':
        for k in keys_input:
            keys[ord(k) - ord('a')] = True
            
    # BFS 탐색 준비
    q = deque([(0, 0)]) # 패딩된 (0,0)에서 시작
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = True
    
    # 열쇠가 없어서 못 들어간 문들의 위치를 저장할 리스트 (인덱스 0: A, 1: B ...)
    doors = [deque() for _ in range(26)]
    
    doc_count = 0
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 체크
            if 0 <= nx < h + 2 and 0 <= ny < w + 2 and not visited[nx][ny]:
                cell = grid[nx][ny]
                
                # 벽이면 통과
                if cell == '*':
                    continue
                
                visited[nx][ny] = True
                
                # 1. 빈 공간(.)
                if cell == '.':
                    q.append((nx, ny))
                
                # 2. 문서($)
                elif cell == '$':
                    doc_count += 1
                    q.append((nx, ny))
                
                # 3. 문(A-Z)
                elif 'A' <= cell <= 'Z':
                    door_idx = ord(cell) - ord('A')
                    # 열쇠가 있으면 큐에 추가
                    if keys[door_idx]:
                        q.append((nx, ny))
                    # 열쇠가 없으면 대기열에 추가
                    else:
                        doors[door_idx].append((nx, ny))
                
                # 4. 열쇠(a-z)
                elif 'a' <= cell <= 'z':
                    q.append((nx, ny))
                    key_idx = ord(cell) - ord('a')
                    
                    # 새로운 열쇠라면
                    if not keys[key_idx]:
                        keys[key_idx] = True
                        # 이 열쇠를 기다리던 문들을 모두 큐에 추가 (이제 갈 수 있음)
                        while doors[key_idx]:
                            qx, qy = doors[key_idx].popleft()
                            q.append((qx, qy))

    print(doc_count)

# 테스트 케이스 개수
t = int(input())
for _ in range(t):
    solve()