import sys
from bisect import bisect_left

# 입력 속도 향상을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(list(map(int, input().split())))

    # 2. A 전봇대 기준으로 오름차순 정렬
    lines.sort(key=lambda x: x[0])

    # B 전봇대의 위치값들만 추출
    b_coords = [line[1] for line in lines]

    # 3. LIS (Longest Increasing Subsequence) 구하기 - O(N log N)
    lis_arr = []        # LIS를 구성하는 값들을 임시 저장 (실제 LIS와 구성은 다를 수 있으나 길이는 정확함)
    record = []         # 각 원소가 LIS의 몇 번째 위치에 들어가는지 기록 (역추적용)

    for b in b_coords:
        # 비어있거나, 현재 값이 LIS 배열의 마지막 값보다 크면 뒤에 추가
        if not lis_arr or b > lis_arr[-1]:
            lis_arr.append(b)
            record.append(len(lis_arr)) # 인덱스 + 1 (길이) 저장
        else:
            # 현재 값이 중간에 들어갈 위치를 이분 탐색으로 찾음
            idx = bisect_left(lis_arr, b)
            lis_arr[idx] = b
            record.append(idx + 1)

    # LIS의 길이 (= 살려야 할 전깃줄의 최대 개수)
    lis_len = len(lis_arr)
    
    # 4. 정답 출력 1: 제거해야 할 전깃줄의 수
    print(n - lis_len)

    # 5. 역추적을 통해 제거해야 할 전깃줄(A좌표) 찾기
    remove_list = []
    
    # 뒤에서부터 탐색하며 LIS 구성 요소가 아닌 것들을 찾음
    # current_lis_len은 찾아야 할 LIS의 현재 순서
    current_lis_len = lis_len
    
    # lines 배열의 뒤에서부터 앞으로 순회
    for i in range(n - 1, -1, -1):
        if record[i] == current_lis_len:
            # LIS에 포함되는 전깃줄임 -> 찾았으니 다음 순서(하나 작은 값)를 찾으러 감
            current_lis_len -= 1
        else:
            # LIS에 포함되지 않는 전깃줄임 -> 제거 대상
            remove_list.append(lines[i][0])

    # 6. 정답 출력 2: 제거되는 전깃줄의 A좌표 (오름차순)
    # 뒤에서부터 탐색했으므로 remove_list는 내림차순 상태 -> 다시 정렬 필요
    remove_list.sort()
    
    for a in remove_list:
        print(a)

if __name__ == "__main__":
    solve()