import sys

# 입력 속도 향상을 위한 readline 사용
input = sys.stdin.readline

# 방향 정의 (문제 조건: 0:우, 1:상, 2:좌, 3:하)
# x는 열(col), y는 행(row)을 의미함에 주의
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def solve():
    n = int(input())
    
    # 격자판 초기화 (좌표가 0~100이므로 101x101 크기 필요)
    grid = [[0] * 101 for _ in range(101)]
    
    for _ in range(n):
        # x, y, 시작 방향 d, 세대 g
        x, y, d, g = map(int, input().split())
        
        # 1. 드래곤 커브의 전체 이동 방향 리스트 생성
        # 0세대 초기화
        moves = [d]
        
        # g세대까지 확장
        for _ in range(g):
            # 현재까지의 이동 방향들을 역순으로 순회
            temp = []
            for i in range(len(moves) - 1, -1, -1):
                # (이전 방향 + 1) % 4 가 새로운 방향
                temp.append((moves[i] + 1) % 4)
            # 기존 리스트에 추가
            moves.extend(temp)
            
        # 2. 격자판에 드래곤 커브 그리기
        # 시작점 표시
        grid[y][x] = 1
        
        # 이동 경로를 따라가며 표시
        curr_x, curr_y = x, y
        for move in moves:
            nx = curr_x + dx[move]
            ny = curr_y + dy[move]
            
            # 좌표 범위 체크 (0 <= x, y <= 100)
            if 0 <= nx <= 100 and 0 <= ny <= 100:
                grid[ny][nx] = 1
                curr_x, curr_y = nx, ny
                
    # 3. 네 꼭짓점이 모두 드래곤 커브인 1x1 정사각형 개수 세기
    ans = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
                ans += 1
                
    print(ans)

if __name__ == "__main__":
    solve()