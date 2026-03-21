import sys

def solve():
    # 입력을 빠르게 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    # 현재 탭 개수와 목표 탭 개수 분리
    current_tabs = list(map(int, input_data[1:N+1]))
    target_tabs = list(map(int, input_data[N+1:2*N+1]))
    
    # 1. 각 줄마다 수정해야 할 차이(diff) 계산
    diff = [target_tabs[i] - current_tabs[i] for i in range(N)]
    
    ans = 0
    # 2. 첫 번째 줄의 절대값만큼은 무조건 작업이 필요함
    curr_move = diff[0]
    ans += abs(curr_move)
    
    # 3. 두 번째 줄부터 순회하며 최소 편집 횟수 계산
    for i in range(1, N):
        # 같은 부호인 경우 (둘 다 늘려야 하거나, 둘 다 줄여야 함)
        if diff[i] * curr_move > 0:
            # 현재 줄이 이전 줄보다 더 많이 수정해야 하는 경우만 차이만큼 더함
            if abs(diff[i]) > abs(curr_move):
                ans += abs(diff[i]) - abs(curr_move)
        # 부호가 다르거나 이전이 0인 경우 (새로운 그룹 시작)
        else:
            ans += abs(diff[i])
            
        # 다음 비교를 위해 현재 값을 갱신
        curr_move = diff[i]
        
    print(ans)

if __name__ == "__main__":
    solve()