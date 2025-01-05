import sys
graph = []
blank = []

# 입력
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 입력에서 0이 있는 좌표 뽑기
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

# 행에서 a와 같은 숫자가 있는지 확인
def checkRow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

# 열에서 같은 숫지가 있는지 확인
def checkCol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

#  현재 좌표의 사각형에서 같은 숫자가 있는지 확인
def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

# DFS들어감
def dfs(idx):
    if idx == len(blank):
        # 모든 점을 채웠으면
        for i in range(9):
            print(*graph[i]) # [1,2,3]을 1 2 3으로 출력해줌
        # 여러 결과 중 하나만 보면되니까 그냥 꺼버리기
        exit(0)
    # 1부터 10 숫자 확인
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]
        # 모두 겹체는게 없으면 숫자 넣기
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            # 현재 0 값 업업데이트
            graph[x][y] = i
            # 다음 0인 곳에서 진행
            dfs(idx+1)
            # 처음 놓은 숫자가 잘못되었으면 다시 0으로 만들고 다른 숫자로 간다.
            graph[x][y] = 0

dfs(0)