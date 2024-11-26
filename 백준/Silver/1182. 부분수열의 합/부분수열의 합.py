import sys
from itertools import combinations

# 부분순열을 하나씩 조지면서 합이 0이되는거를 한다.
# 근데 생각해보니 부분순열을 그 뭐냐 중복되는거 제외하고 조합으로 하면 됨
# 근데 자기 자신도 추가해야됨

n, s = map(int, sys.stdin.readline().rstrip().split(" "))
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
count = 0

for i in range(1, len(input_list)+1):
    for combination in list(combinations(input_list, i)):
        if sum(combination) == s:
            count += 1

print(count)

