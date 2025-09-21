import sys
input_data = sys.stdin.read().strip().split()
dice = list(map(int, input_data))  # 10개의 주사위 값

# 보드 그래프 구성
# 각 노드는 다음과 같은 의미를 갖습니다.
# 0: 시작, 21: 도착(END)
# 1~20: 메인 경로(2,4,6,...,40)
# 22,23,24: 10에서 파란길(13,16,19)
# 28,29: 20에서 파란길(22,24)
# 30,31,32: 30에서 파란길(28,27,26)
# 25: 25(세 갈래가 합류)
# 26: 30, 27: 35 (25 이후 공통 경로)
#
# next1: 일반(빨간) 진행 포인터
# next2: 파란 칸에서 처음 한 칸 이동 시 타는 파란 포인터 (그 외에는 next1로 진행)
#
# 점수(score): 도착(21)은 0점 취급.

# 다음 칸(빨간길)
next1 = [0] * 33
# 파란길 진입(해당 칸에서 첫 스텝만 파란길)
next2 = [-1] * 33
# 점수
score = [0] * 33

# 메인 경로 0(start) -> 1(2) -> ... -> 20(40) -> 21(end)
for i, s in enumerate(range(0, 41, 2)):
    idx = i  # 0..20
    score[idx] = s
for i in range(0, 20):
    next1[i] = i + 1
next1[20] = 21  # 40 다음은 END
next1[21] = 21  # END에서 계속 END

# 파란길 진입 지점: 5(10), 10(20), 15(30)
# 10의 파란길: 22(13) -> 23(16) -> 24(19) -> 25(25) -> 26(30) -> 27(35) -> 20(40) -> 21
next2[5] = 22
score[22], score[23], score[24] = 13, 16, 19
next1[22], next1[23], next1[24] = 23, 24, 25

# 20의 파란길: 28(22) -> 29(24) -> 25(25) -> ...
next2[10] = 28
score[28], score[29] = 22, 24
next1[28], next1[29] = 29, 25

# 30의 파란길: 30(28) -> 31(27) -> 32(26) -> 25(25) -> ...
next2[15] = 30
score[30], score[31], score[32] = 28, 27, 26
next1[30], next1[31], next1[32] = 31, 32, 25

# 합류 지점(공통 경로): 25(25) -> 26(30) -> 27(35) -> 20(40) -> 21
score[25], score[26], score[27] = 25, 30, 35
next1[25], next1[26], next1[27] = 26, 27, 20

def move(pos, step):
    """현재 pos에서 step만큼 이동했을 때의 최종 위치를 반환."""
    if pos == 21:
        return 21
    # 첫 스텝: 파란길 진입 가능한 칸(5,10,15)이면 next2, 아니면 next1
    if pos in (5, 10, 15) and next2[pos] != -1:
        cur = next2[pos]
    else:
        cur = next1[pos]
    step -= 1
    # 남은 스텝은 모두 next1로 진행
    while step > 0 and cur != 21:
        cur = next1[cur]
        step -= 1
    return cur

ans = 0

def dfs(turn, positions, total):
    # positions: 말 4개의 현재 위치 인덱스(0~21)
    # turn: 주사위 인덱스(0~9), total: 지금까지 점수
    global ans
    if turn == 10:
        if total > ans:
            ans = total
        return

    d = dice[turn]
    # 4개의 말 중 하나를 선택해서 이동
    for i in range(4):
        cur = positions[i]
        if cur == 21:
            # 이미 도착한 말은 움직여도 그대로(무의미), 그래도 시도는 가능
            new_pos = 21
        else:
            new_pos = move(cur, d)

        # 도착(21)이 아닌데, 이미 다른 말이 그 칸에 있으면 금지
        if new_pos != 21 and any(positions[j] == new_pos for j in range(4) if j != i):
            continue

        gained = 0 if new_pos == 21 else score[new_pos]

        # 상태 변경
        prev = positions[i]
        positions[i] = new_pos
        dfs(turn + 1, positions, total + gained)
        positions[i] = prev  # 복구

# 초기 말 위치는 모두 0(시작)
dfs(0, [0, 0, 0, 0], 0)
print(ans)