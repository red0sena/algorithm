import sys

# 입력 처리
# sys.stdin.readline()을 사용하면 로컬 테스트 시 입력을 직접 넣어야 하므로,
# 다양한 테스트 케이스를 쉽게 확인하기 위해 문자열 입력을 가정합니다.
# 백준에 제출할 때는 아래 두 줄을 활성화하세요.
# input_data = sys.stdin.readline().strip().split()
# dice = list(map(int, input_data))

# 예제 입력
dice = list(map(int, input().split()))


# --- 게임판 설정 ---
# 각 인덱스는 칸의 위치를 나타냅니다.
# (점수, 일반 경로 다음 칸, 지름길 다음 칸) 형태의 튜플로 관리합니다.
# 지름길이 없는 경우 -1로 표시합니다.
# 0: 시작, 21-26: 10->, 27-28: 20->, 29-31: 30->, 32-34: 중앙, 35: 도착
board = [
    # 0~20: 바깥 경로 (점수 0 ~ 40)
    (0, 1, -1), (2, 2, -1), (4, 3, -1), (6, 4, -1), (8, 5, -1), (10, 6, 21), # 0-5
    (12, 7, -1), (14, 8, -1), (16, 9, -1), (18, 10, -1), (20, 11, 27), # 6-10
    (22, 12, -1), (24, 13, -1), (26, 14, -1), (28, 15, -1), (30, 16, 29), # 11-15
    (32, 17, -1), (34, 18, -1), (36, 19, -1), (38, 20, -1), (40, 35, -1), # 16-20
    # 21~26: 10에서 시작하는 지름길
    (13, 22, -1), (16, 23, -1), (19, 32, -1), # 21-23
    (0, 0, 0), (0, 0, 0), (0, 0, 0), # 24-26 (사용 안함)
    # 27~28: 20에서 시작하는 지름길
    (22, 28, -1), (24, 32, -1), # 27-28
    # 29~31: 30에서 시작하는 지름길
    (28, 30, -1), (27, 31, -1), (26, 32, -1), # 29-31
    # 32~34: 중앙 공통 경로
    (25, 33, -1), (30, 34, -1), (35, 20, -1), # 32-34
    # 35: 도착
    (0, 35, -1)
]

max_score = 0
pieces = [0] * 4  # 4개 말의 현재 위치 (0은 시작점)

def solve(turn, current_score):
    """
    백트래킹을 이용해 모든 경우를 탐색하는 함수
    Args:
        turn (int): 현재 주사위 차례 (0-9)
        current_score (int): 현재까지의 누적 점수
    """
    global max_score

    # 10번의 턴을 모두 마쳤으면 최댓값 갱신
    if turn == 10:
        max_score = max(max_score, current_score)
        return

    dice_num = dice[turn]

    # 4개의 말 중 하나를 선택하여 이동
    for i in range(4):
        start_pos = pieces[i]

        # 이미 도착한 말은 움직일 수 없음
        if start_pos == 35:
            continue

        # 1. 말 이동
        current_pos = start_pos
        # 첫 번째 이동: 지름길이 있는지 확인
        score_val, next_pos_normal, next_pos_shortcut = board[current_pos]
        if next_pos_shortcut != -1:
            current_pos = next_pos_shortcut
        else:
            current_pos = next_pos_normal

        # 나머지 이동
        for _ in range(dice_num - 1):
            if current_pos == 35: break # 이동 중 도착하면 멈춤
            current_pos = board[current_pos][1]

        # 2. 유효성 검사: 이동을 마친 칸에 다른 말이 있는지 확인
        # (도착 지점은 예외)
        if current_pos != 35:
            is_occupied = False
            for j in range(4):
                if i != j and pieces[j] == current_pos:
                    is_occupied = True
                    break
            if is_occupied:
                continue
        
        # 3. 상태 업데이트 및 재귀 호출 (백트래킹)
        pieces[i] = current_pos # 말 위치 변경
        solve(turn + 1, current_score + board[current_pos][0])
        pieces[i] = start_pos   # 다음 경우의 수를 위해 말 위치 원상복구

# 탐색 시작
solve(0, 0)
print(max_score)