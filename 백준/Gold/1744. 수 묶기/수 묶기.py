import sys 
from collections import deque

n = int(sys.stdin.readline())

positive_numbers = []
is_zero = False
negative_numbers = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    else:
        is_zero = True


positive_numbers.sort()
negative_numbers.sort()

positive_queue = deque(positive_numbers)
negative_queue = deque(negative_numbers)


sum = 0 
else_num = []
while positive_queue:
    if len(positive_queue) <= 1:
        else_num.append(positive_queue.pop())
        break
    big_one = positive_queue.pop()
    small_one = positive_queue.pop()
    if small_one == 1 or big_one == 1:
        else_num.append(small_one)
        else_num.append(big_one)
        continue
    sum += (big_one * small_one)
for num in else_num:
    sum += num

else_num = []
while negative_queue:
    if len(negative_queue) <= 1:
        else_num.append(negative_queue.pop())
        break
    big_one = negative_queue.popleft()
    small_one = negative_queue.popleft()
    sum += (big_one * small_one)

for num in else_num:
    if is_zero:
        is_zero = False
    else:
        sum += num


print(sum)