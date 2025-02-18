N, L = map(int, input().split())

input_list = [list(map(int, input().split())) for _ in range(N)]
res = 0

for i in range(N):
    visited = [-1] * N
    for j in range(N-1):
        if input_list[i][j] + 1 == input_list[i][j+1]: # 만약 다음 칸이 지금칸보다 1 더 크다면
            if j-L+1 >= 0:
                if all(input_list[i][j] == num for num in (input_list[i][j-L+1:j+1])): # 게단을 놓을 공간이 되는지 확인
                    already_visited_flag = False
                    for k in range(j-L+1, j+1): # 이전에 계단을 놓은 적 있는지 확인
                        if visited[k] != -1:
                            already_visited_flag = True # 이전에 계단을 놓았으면 계단 못탐
                            break
                        else:
                            visited[k] = 1
                    if already_visited_flag:
                        break
                else:
                    break
            else:
                break
        elif input_list[i][j] - 1 == input_list[i][j+1]:
            if j+L < N:
                if all(input_list[i][j+1] == num for num in (input_list[i][j+1:j+L+1])): # 게단을 놓을 공간이 되는지 확인
                    already_visited_flag = False
                    for k in range(j+1, j+L+1):
                        if visited[k] != -1:
                            already_visited_flag = True
                            break
                        else:
                            visited[k] = 1
                    if already_visited_flag:
                        break
                else:
                    break
            else:
                break
        elif input_list[i][j] != input_list[i][j+1]:
            break

        if j == N-2:
            res += 1
            break


input_list2 = []
for i in range(N):
    a = []
    for j in range(N):
        a.append(input_list[j][i])
    input_list2.append(a)

for i in range(N):
    visited = [-1] * N
    for j in range(N-1):
        if input_list2[i][j] + 1 == input_list2[i][j+1]: # 만약 다음 칸이 지금칸보다 1 더 크다면
            if j-L+1 >= 0:
                if all(input_list2[i][j] == num for num in (input_list2[i][j-L+1:j+1])): # 게단을 놓을 공간이 되는지 확인
                    already_visited_flag = False
                    for k in range(j-L+1, j+1): # 이전에 계단을 놓은 적 있는지 확인
                        if visited[k] != -1:
                            already_visited_flag = True # 이전에 계단을 놓았으면 계단 못탐
                            break
                        else:
                            visited[k] = 1
                    if already_visited_flag:
                        break
                else:
                    break
            else:
                break
        elif input_list2[i][j] - 1 == input_list2[i][j+1]:
            if j+L < N:
                if all(input_list2[i][j+1] == num for num in (input_list2[i][j+1:j+L+1])): # 게단을 놓을 공간이 되는지 확인
                    already_visited_flag = False
                    for k in range(j+1, j+L+1):
                        if visited[k] != -1:
                            already_visited_flag = True
                            break
                        else:
                            visited[k] = 1
                    if already_visited_flag:
                        break
                else:
                    break
            else:
                break
        elif input_list2[i][j] != input_list2[i][j+1]:
            break

        if j == N-2:
            res += 1
            break




print(res)
