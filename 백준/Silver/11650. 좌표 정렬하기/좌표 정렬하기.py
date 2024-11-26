import sys


n = int(sys.stdin.readline().rstrip())
x_y_list = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    x_y_list.append((x, y))


x_y_list = sorted(x_y_list)

for tuple in x_y_list:
    print(tuple[0], tuple[1])
