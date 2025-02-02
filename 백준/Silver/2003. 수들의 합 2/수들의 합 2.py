import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

input_list = list(map(int, sys.stdin.readline().rstrip().split()))

prefix = [0]

count = 0

for i in range(n):
    add = prefix[i] + input_list[i]
    if add == m or (add - m) in prefix:
        count += 1
    prefix.append(add)

print(count)