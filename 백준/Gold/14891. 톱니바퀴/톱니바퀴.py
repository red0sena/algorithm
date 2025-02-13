from collections import deque
input_list = [deque(map(int, input())) for _ in range(4)]

k = int(input())


# 일단 현재 바퀴는 무조건 돌리고 그 다음에 index가 혀용하는 범위 내에서 좌우로 벌린다. 재귀로 구현하면 될 듯?
def roll_wheel(wheel_index, rotation_direction, come_from):
    # 바퀴 가져오기 여기에 들어왔으면 무조건 돌려야 한다.
    wheel = input_list[wheel_index]
    if rotation_direction == 1:
        pop_val = wheel.pop()
        wheel.appendleft(pop_val)
        input_list[wheel_index] = wheel
    else:
        pop_val = wheel.popleft()
        wheel.append(pop_val)
        input_list[wheel_index] = wheel

    # 바퀴를 돌리기전 오른쪽 왼쪽 바퀴를 확인한다.
    # 극이 같다면 그쪽으로 들어가고 아니면 안들어간다.
    if wheel_index - 1 >= 0 and come_from != -1: # 왼쪽에서 오지 않았다면 왼쪽 바퀴 확인
        left_wheel = input_list[wheel_index - 1]
        if left_wheel[2] != wheel[6+(rotation_direction)]: # 극이 다르다면 돌려야함, 지금과 반대 방향으로
            if rotation_direction == 1:
                roll_wheel(wheel_index - 1, -1, 1)
            else:
                roll_wheel(wheel_index - 1, 1, 1)
    if wheel_index + 1 <= 3 and come_from != 1: # 오른쪽에서 오지 않았다면 오른쪽 바퀴 확인
        right_wheel = input_list[wheel_index + 1]
        if right_wheel[6] != wheel[2+(rotation_direction)]: # 오른쪽 바퀴와 극이 다르다면 돌려야 함, 지금과 반대 방향으로
            if rotation_direction == 1:
                roll_wheel(wheel_index + 1, -1, -1)
            else:
                roll_wheel(wheel_index + 1, 1, -1)








for i in range(k):
    a, b = map(int, input().split())
    # 돌아가야 할 바퀴 번호와 시계 반시계 방향만 알면 저체 톱니의 회전 방향을 알 수 있다.
    roll_wheel(a-1,b, 0)

res = 0
for i in range(4):
    if input_list[i][0] == 1:
        res += (1*(2**i))


print(res)

