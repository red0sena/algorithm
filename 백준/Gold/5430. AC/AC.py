from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
# sys.stdin = open('input.txt')
t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    input_list = deque(eval(input()))
    error_flag = False      # 에러 발생 여부를 추적하는 플래그
    reversed_flag = False   # 리스트의 순서 상태

    for command in p:
        if command == "R":
            reversed_flag = not reversed_flag
        elif command == "D":
            if input_list:
                if not reversed_flag:
                    input_list.popleft()
                else:
                    input_list.pop()
            else:
                print('error')
                error_flag = True
                break  # 에러 발생 시 반복문 종료

    if not error_flag:
        if reversed_flag:
            input_list.reverse()
        print("[" + ",".join(map(str, input_list)) + "]")
