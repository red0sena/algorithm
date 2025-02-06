import sys
from collections import Counter

input = sys.stdin.readline

# 상근이가 가진 카드의 개수
N = int(input().strip())
# 카드에 적힌 숫자 리스트
cards = list(map(int, input().split()))
# 각 카드에 적힌 숫자의 빈도수 계산
card_count = Counter(cards)

# 쿼리의 개수
M = int(input().strip())
# 쿼리 숫자 리스트
queries = list(map(int, input().split()))

# 각 쿼리에 대해 상근이가 가진 카드 수 출력
result = []
for number in queries:
    result.append(str(card_count[number]))

# 결과 출력 (공백으로 구분)
print(" ".join(result))
