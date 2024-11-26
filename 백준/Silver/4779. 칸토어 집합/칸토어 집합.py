import sys


def recursive(n):
    if n == 0:
        return '-'
    ans = recursive(n - 1)
    return ans + (' ' * (3 ** (n-1))) + ans

while True:
	try:
         N = int(sys.stdin.readline().rstrip())
         print(recursive(N))
	except:
		 break