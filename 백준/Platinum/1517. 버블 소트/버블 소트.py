import sys

def merge_sort(arr, temp_arr, left, right):
    """병합 정렬을 수행하면서 역순 쌍의 개수를 계산"""
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    inv_count = 0
    
    # 왼쪽 부분 배열에서의 역순 쌍 개수
    inv_count += merge_sort(arr, temp_arr, left, mid)
    # 오른쪽 부분 배열에서의 역순 쌍 개수
    inv_count += merge_sort(arr, temp_arr, mid + 1, right)
    # 병합 과정에서의 역순 쌍 개수
    inv_count += merge(arr, temp_arr, left, mid, right)
    
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    """두 정렬된 부분 배열을 병합하면서 역순 쌍을 계산"""
    i = left        # 왼쪽 부분 배열의 시작 인덱스
    j = mid + 1     # 오른쪽 부분 배열의 시작 인덱스
    k = left        # 병합된 배열의 시작 인덱스
    inv_count = 0
    
    # 두 부분 배열을 병합
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            # arr[i] > arr[j]인 경우, arr[i]부터 arr[mid]까지 모두 arr[j]보다 크므로
            # (mid - i + 1)개의 역순 쌍이 발생
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    
    # 왼쪽 부분 배열의 남은 요소들을 복사
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    # 오른쪽 부분 배열의 남은 요소들을 복사
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    # 정렬된 결과를 원래 배열에 복사
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

# 입력 받기
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# 임시 배열 생성
temp_arr = [0] * n

# 병합 정렬을 수행하면서 swap 횟수(역순 쌍의 개수) 계산
result = merge_sort(arr, temp_arr, 0, n - 1)

# 결과 출력
print(result)
