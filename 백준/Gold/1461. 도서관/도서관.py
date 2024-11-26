import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

# 입력을 받으면서 바로 음수, 양수 리스트로 나누기
negatives = []
positives = []
for num in map(int, sys.stdin.readline().rstrip().split()):
    if num < 0:
        negatives.append(num)
    else:
        positives.append(num)

# 각각 정렬
negatives = sorted(negatives)  # 음수 정렬
positives = sorted(positives, reverse=True)  # 양수 정렬

res = []

for i in range(0, len(negatives), m):
    res.append(negatives[i:i+2])

for i in range(0, len(positives), m):
    res.append(positives[i:i+2])

res = sorted(res, key=lambda x : -abs(x[0]))
suma = 0
for i in range(0, len(res)):
    if i == 0:
        suma += abs(res[i][0])
    else:
        suma += abs(res[i][0]) * 2


print(suma)
