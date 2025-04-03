from collections import deque




n, k = map(int, input().split())

input_list = list(map(int, input().split()))

conveyor_belt = deque(input_list)

robot_loc = deque([0]*n)


# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

time_sec = 0
count = 0
while True:

    # 1. 돌리고~
    pop_v = conveyor_belt.pop()
    conveyor_belt.appendleft(pop_v)

    pop_v2 = robot_loc.pop()
    robot_loc.appendleft(pop_v2)
    robot_loc[n-1] = 0

    # 2. 내리는 직전 부분부터 역순으로
    for i in range(n-2, -1, -1):
        if robot_loc[i] == 1: # 현재칸이 로봇이 있고
            if robot_loc[i+1] == 0: # 이동하려는 칸에 로봇이 없으며
                if conveyor_belt[i+1] > 0: # 그 칸의 컨베이어 벨트 내구도가 1 이상이면
                    robot_loc[i] = 0 # 현재칸은 없애기
                    if i+1 == n-1: # 다음칸이 로봇 내리는 경우
                        robot_loc[i+1] = 0
                    else: # 내리지 않는 경우
                        robot_loc[i+1] = 1
                    conveyor_belt[i+1] -= 1 # 이동 시 내구도 1 감소
                    if conveyor_belt[i+1] == 0: # 이동해서 내구도가 0이되면 count
                        count += 1


    # 3.
    if conveyor_belt[0] != 0: #  올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        robot_loc[0] = 1
        conveyor_belt[0] -= 1
        if conveyor_belt[0] == 0: # 내구도 0되면 count
            count += 1

    time_sec += 1
    if count >= k: # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
        print(time_sec)
        break

