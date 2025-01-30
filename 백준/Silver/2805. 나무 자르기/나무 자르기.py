import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 1) 정렬
trees.sort()

# 2) 누적합(prefix sum) 계산
prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + trees[i-1]
    
# 이분 탐색 범위 설정
left, right = 0, trees[-1]
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    # 3) mid 초과 구간 찾기: 이분 탐색 (bisect)
    #  trees에서 mid보다 큰 구간의 시작 index
    idx = bisect.bisect_right(trees, mid)  
    # trees[idx] 이상인 원소들이 mid보다 큼
    
    # 4) mid보다 큰 나무들 합 구하기
    #    나무들을 모두 더해놓은 prefix[N] - prefix[idx] = (trees[idx] + ... + trees[N-1])의 합
    #    각 나무는 mid 이상이므로, 잘린 양은 (합 - mid * (개수))
    #   개수는 (n - idx)
    cut_sum = prefix[n] - prefix[idx] - mid * (n - idx)
    
    # 이 cut_sum이 우리가 필요한 나무(m)보다 크거나 같으면 -> 더 위에서 잘라도 됨
    if cut_sum >= m:
        answer = mid  # 만족 가능한 mid, 갱신
        left = mid + 1
    else:
        right = mid - 1

print(answer)
