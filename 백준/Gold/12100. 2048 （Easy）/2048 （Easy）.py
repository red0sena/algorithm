import sys

# 입력을 빠르게 받기 위함
input = sys.stdin.readline

N = int(input())
initial_board = [list(map(int, input().split())) for _ in range(N)]
max_block_value = 0

# 90도 시계방향 회전
def rotate_90_clockwise(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[j][N - 1 - i] = board[i][j]
    return new_board

# '왼쪽'으로 밀기 (핵심 로직)
def move_left(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        # 1. 0이 아닌 숫자만 임시 리스트에 저장 (Squeeze)
        temp = [val for val in board[i] if val != 0]
        
        # 2. 합치기 (Merge)
        merged = []
        k = 0
        while k < len(temp):
            if k + 1 < len(temp) and temp[k] == temp[k + 1]:
                # 두 숫자가 같으면 합치기
                merged.append(temp[k] * 2)
                k += 2 # 숫자 두 개를 사용했으므로 2칸 점프
            else:
                # 합칠 수 없으면 그냥 추가
                merged.append(temp[k])
                k += 1 # 숫자 한 개만 사용
        
        # 3. 결과(merged)를 new_board에 반영
        for j in range(len(merged)):
            new_board[i][j] = merged[j]
            
    return new_board

# DFS 함수 (모든 경우의 수 탐색)
def dfs(board, count):
    global max_block_value
    
    # 5번 이동이 끝났을 때
    if count == 5:
        # 현재 보드에서 가장 큰 값 찾기
        current_max = 0
        for i in range(N):
            for j in range(N):
                current_max = max(current_max, board[i][j])
        
        # 전역 최대값 갱신
        max_block_value = max(max_block_value, current_max)
        return

    # --- 4방향 이동 ---
    
    # 1. 위로 이동
    # (반시계 90도 회전 -> 왼쪽 밀기 -> 시계 90도 회전)
    b_up = rotate_90_clockwise(rotate_90_clockwise(rotate_90_clockwise(board)))
    b_up = move_left(b_up)
    b_up = rotate_90_clockwise(b_up)
    dfs(b_up, count + 1)

    # 2. 아래로 이동
    # (시계 90도 회전 -> 왼쪽 밀기 -> 반시계 90도 회전)
    b_down = rotate_90_clockwise(board)
    b_down = move_left(b_down)
    b_down = rotate_90_clockwise(rotate_90_clockwise(rotate_90_clockwise(b_down)))
    dfs(b_down, count + 1)

    # 3. 왼쪽으로 이동
    b_left = move_left(board)
    dfs(b_left, count + 1)
    
    # 4. 오른쪽으로 이동
    # (180도 회전 -> 왼쪽 밀기 -> 180도 회전)
    b_right = rotate_90_clockwise(rotate_90_clockwise(board))
    b_right = move_left(b_right)
    b_right = rotate_90_clockwise(rotate_90_clockwise(b_right))
    dfs(b_right, count + 1)


# --- 메인 실행 ---

# (중요) 초기 상태의 값도 최대값 후보가 될 수 있음 (N=1일 경우 등)
for i in range(N):
    for j in range(N):
        max_block_value = max(max_block_value, initial_board[i][j])

# DFS 시작
dfs(initial_board, 0)

print(max_block_value)