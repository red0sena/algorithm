import sys
from itertools import permutations

input = sys.stdin.readline

K, M = map(int, input().split())

MAX = 100000

# 소수 구하기
is_prime = [True] * MAX
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX, i):
            is_prime[j] = False

primes = [i for i in range(2, MAX) if is_prime[i]]

# 두 소수 합
prime_sum = [False] * MAX

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        s = primes[i] + primes[j]
        if s >= MAX:
            break
        prime_sum[s] = True


# 두 소수 곱
prime_mul = [False] * MAX

for i in range(len(primes)):
    for j in range(i, len(primes)):
        p = primes[i] * primes[j]
        if p >= MAX:
            break
        prime_mul[p] = True


answer = 0

for p in permutations(range(10), K):

    if p[0] == 0:
        continue

    num = int(''.join(map(str, p)))

    # 조건1
    if not prime_sum[num]:
        continue

    # 조건2
    x = num
    while x % M == 0:
        x //= M

    if prime_mul[x]:
        answer += 1


print(answer)