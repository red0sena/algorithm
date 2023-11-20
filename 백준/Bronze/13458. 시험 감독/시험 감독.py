import sys
import math

N = int(sys.stdin.readline())

chum_jang_list = list(map(int, sys.stdin.readline().split()))

C, B = map(int, sys.stdin.readline().split())

res = 0
for chum_jang_in_1 in chum_jang_list:
    chum_jang_in_1 = chum_jang_in_1 - C
    res += 1
    if chum_jang_in_1 <= 0:
        continue
    else:
        res += math.ceil(chum_jang_in_1/B)

print(res)