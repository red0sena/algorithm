import sys

input_str = sys.stdin.readline().rstrip()
boom_str = sys.stdin.readline().rstrip()

boom_str_len = len(boom_str)
stack = []
for i in range(len(input_str)):
    stack.append(input_str[i])
    if ''.join(stack[-boom_str_len:]) == boom_str:
        for _ in range(boom_str_len):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')


