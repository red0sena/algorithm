import math
n = int(input())
def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


prime_list = [0, 2]
for i in range(3, n+1, 2):
    if is_prime(i):
        prime_list.append(prime_list[-1] + i)


current_sum = 0
start, end = 0, 0
count = 0

while True:
    val = prime_list[end] - prime_list[start]
    if val == n:
        count += 1
        start += 1
    elif val < n and end < len(prime_list)-1:
        end += 1
    elif val > n:
        start += 1
    else:
        break

print(count)