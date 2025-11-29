import sys

# 입력 속도 향상을 위한 설정
input = sys.stdin.readline

# 스도쿠 보드 입력 받기
board = []
for _ in range(9):
    board.append(list(map(int, list(input().strip()))))

# 빈 칸(0)의 좌표만 미리 저장 (좌표 리스트)
zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))

# 유효성 검사 함수
def check(r, c, num):
    # 1. 같은 행에 num이 있는지 확인
    for i in range(9):
        if board[r][i] == num:
            return False
            
    # 2. 같은 열에 num이 있는지 확인
    for i in range(9):
        if board[i][c] == num:
            return False
            
    # 3. 3x3 박스에 num이 있는지 확인
    # (nr, nc)는 해당 3x3 박스의 시작 좌표
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[nr + i][nc + j] == num:
                return False
                
    return True

# 백트래킹 (DFS) 함수
def dfs(idx):
    # 종료 조건: 모든 빈 칸을 다 채웠을 때
    if idx == len(zeros):
        for row in board:
            print(''.join(map(str, row)))
        sys.exit(0) # 답을 하나 찾으면 바로 프로그램 전체 종료

    # 현재 채워야 할 빈 칸의 좌표 가져오기
    r, c = zeros[idx]
    
    # 1부터 9까지 넣어보기
    for num in range(1, 10):
        # 해당 자리에 num을 놓을 수 있는지 확인
        if check(r, c, num):
            board[r][c] = num # 숫자 배치
            dfs(idx + 1)      # 다음 빈 칸으로 이동
            board[r][c] = 0   # (백트래킹) 다시 되돌리기

# 실행
dfs(0)