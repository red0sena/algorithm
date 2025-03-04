import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
# 보드: 각 행은 가로선 위치, 열은 1 ~ n (양쪽 경계는 0과 n로 사용)
board = [[0] * (n + 1) for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a - 1][b] = 1

def go_down():
    # 각 세로선 i에서 출발하여, 사다리 끝까지 내려갔을 때 i로 도착하는지 시뮬레이션
    for start in range(1, n+1):
        pos = start
        for i in range(h):
            if board[i][pos] == 1:       # 오른쪽으로 이동
                pos += 1
            elif pos > 1 and board[i][pos-1] == 1:  # 왼쪽으로 이동
                pos -= 1
        if pos != start:
            return False
    return True

# 모든 후보 위치를 (row, col) 형태로 생성(가로선은 col 1 ~ n-1에서만 놓을 수 있음)
candidates = [(i, j) for i in range(h) for j in range(1, n)]

def dfs(count, start, target):
    # 이미 target개를 놓은 경우, 사다리 결과가 올바른지 확인
    if count == target:
        if go_down():
            print(target)
            sys.exit(0)
        return

    for idx in range(start, len(candidates)):
        i, j = candidates[idx]
        # 현재 위치에 가로선이 없는지 체크
        if board[i][j] != 0:
            continue
        # 왼쪽, 오른쪽 인접한 곳에 이미 가로선이 있으면 놓을 수 없음
        if j - 1 >= 1 and board[i][j-1] == 1:
            continue
        if j + 1 <= n - 1 and board[i][j+1] == 1:
            continue

        board[i][j] = 1
        dfs(count + 1, idx + 1, target)
        board[i][j] = 0

# 0 ~ 3개의 가로선을 추가해서 문제 조건 만족 여부 확인
for target in range(4):
    dfs(0, 0, target)

print(-1)
