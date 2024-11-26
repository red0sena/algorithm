import sys


n = int(sys.stdin.readline().rstrip())
num_list = []
for i in range(1, n+1):
    num_list.append(i)
ans = []
check = [False] * n
def recursive(level):
    if level == n:
        for i in ans:
            print(i, end=" ")
        print()
        return

    for i in range(0, n):
        if check[i] == True:
            continue
        check[i] = True
        ans.append(num_list[i])
        recursive(level+1)
        check[i] = False
        ans.pop()

recursive(0)