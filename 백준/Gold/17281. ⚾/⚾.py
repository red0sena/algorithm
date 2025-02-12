import sys, itertools

N = int(input())

innings = [list(map(int, input().split())) for _ in range(N)]

# 1번 선수는 반드시 4번 타자(인덱스 3)에 배치되어야 하므로 나머지 선수(2~9번)에 대해 순열을 생성
players = [i for i in range(2, 10)]
max_score = 0

# 모든 가능한 타순 순열에 대해 시뮬레이션
for perm in itertools.permutations(players):
    # 타순: 처음 3명 + [1번 선수] + 나머지 5명
    order = list(perm[:3]) + [1] + list(perm[3:])
    score = 0
    batting_index = 0  # 타순에서 현재 타자 인덱스 (0~8)

    # 각 이닝 시뮬레이션 (이닝 간 타순은 이어집니다.)
    for inning in innings:
        outs = 0
        # 1루,2루,3루 주자 상태를 각각 b1, b2, b3 로 관리 (0: 없음, 1: 있음)
        b1 = b2 = b3 = 0
        while outs < 3:
            # 현재 타자가 얻는 결과. inning 리스트의 인덱스는 선수 번호-1 입니다.
            res = inning[order[batting_index] - 1]
            if res == 0:
                outs += 1
            elif res == 1:
                # 안타: 모든 주자가 한 루씩 진루 -> 3루에 있던 주자는 득점
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif res == 2:
                # 2루타: 모든 주자가 두 루씩 진루 -> 2루, 3루에 있던 주자는 득점, 1루에 있던 주자는 3루로
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif res == 3:
                # 3루타: 모든 주자가 세 루씩 진루 -> 모든 주자 득점, 타자는 3루로
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            elif res == 4:
                # 홈런: 모든 주자와 타자 득점, 베이스 초기화
                score += b3 + b2 + b1 + 1
                b3 = b2 = b1 = 0
            batting_index += 1
            if batting_index >= 9:
                batting_index = 0
    if score > max_score:
        max_score = score
print(str(max_score))


