from collections import deque
import sys

input = lambda:sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    input_list = deque(eval(input()))
    point = True
    error_flag = False
    for command in p:
        if command == "R":
            point = not point
        elif command == "D":
            try:
                if point:
                    input_list.popleft()
                else:
                    input_list.pop()
            except:
                print('error')
                error_flag = True
                break

    if not error_flag:
        if not point:
            input_list.reverse()

        print("[" + ",".join(map(str, input_list)) + "]")

