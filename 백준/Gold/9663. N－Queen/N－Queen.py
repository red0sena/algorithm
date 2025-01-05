from collections import deque

n = int(input())

queen_count = 0
columns = [0] * n # 자신의 열에 퀸이 놓여져 있는지 체크
tl_to_br = [0] * (2*n+1) # 왼쪽 위에서(top left) 오른쪽 아래로(bottom right)이어지는 대각선에 퀸이 놓여져 있는지 체크
tr_to_bl = [0] * (2*n+1) # 오른쪽 위에서(top right) 왼쪽 아래로(bottom left)이어지는 대간선에 퀸이 놓여져 있는지 체크
res = 0

# DFS
def dfs(i):
    global queen_count, res
    # 만약 목표 했던 퀸의 개수를 모두 채우면 경우의 수 1 더함
    if queen_count == n:
        res += 1
    # 반복문 (열)을 돌어가며 놓을 수 있는지 확인
    for j in range(n):
        # columns[j] == 0 열에 대한 체크
        # tr_to_bl[i + j] == 0 인덱스의 x+y값이 tl_to_br 대각선 인덱스
        # tl_to_br[i - j + 1] == 0 인덱스의 x-y+1 값이  tl_to_br의 대각선 인덱스
        if columns[j] == 0 and tr_to_bl[i + j] == 0 and tl_to_br[i - j] == 0: # 이게 가지치기 랍니다.
            # 모든 조건을 통과했으니 + 1
            # 퀸의 범위에 대한 정보도 없데이트
            queen_count += 1
            columns[j] = 1
            tr_to_bl[i + j] = 1
            tl_to_br[i - j] = 1
            dfs(i+1)
            # 모든 퀸의 개수를 채웠으니 이제 다음것에 하러 가야함 지금 놓여져 있는 퀸 빼기
            # 퀸의 범위에 대한 정보도 없데이트
            queen_count -= 1
            columns[j] = 0
            tr_to_bl[i + j] = 0
            tl_to_br[i - j] = 0

# 첫 행부터 시작
dfs(0)
print(res)