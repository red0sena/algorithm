from collections import deque

n, m = map(int, input().split())
input_list = list(map(int, input().split()))

input_list.sort()
q = deque(input_list)
count = 0
if len(q) < 2:
    print(0)
else:
    while len(q) > 1:
        sum_val = q.pop()
        flag = True
        while sum_val < m or flag:
            flag = False
            if not q:
                break
            min_val = q.popleft()
            sum_val += min_val
        if sum_val >= m:
            count += 1

    print(count)
