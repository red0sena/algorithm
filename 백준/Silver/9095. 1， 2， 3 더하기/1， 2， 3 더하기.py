import sys

t = int(sys.stdin.readline().rstrip())

count = 0

def recursive(n):
    global count
    if n < 0:
        return
    if n == 0:
        count += 1
        return
    else:
        recursive(n-1)
        recursive(n-2)
        recursive(n-3)



for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    recursive(n-1)
    recursive(n-2)
    recursive(n-3)
    print(count)
    count = 0

