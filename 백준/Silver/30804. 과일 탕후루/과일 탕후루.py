def max_fruit_tanghulu(N, fruits):
    # 최대 길이 저장
    max_length = 0
    # 과일 종류별 개수 저장
    fruit_count = {}
    # 왼쪽 포인터
    left = 0
    
    # 오른쪽 포인터로 배열 순회
    for right in range(N):
        # 현재 과일 추가
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
        
        # 과일 종류가 2개를 초과하면 윈도우 축소
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        
        # 현재 윈도우 크기로 최대 길이 갱신
        max_length = max(max_length, right - left + 1)
    
    return max_length

# 입력 처리
N = int(input())
fruits = list(map(int, input().split()))

# 결과 출력
print(max_fruit_tanghulu(N, fruits))