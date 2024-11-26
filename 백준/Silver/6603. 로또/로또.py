import sys

def recursive(index, level):
    if level == 6:
        for i in ans:
            print(i, end=" ")
        print()
        return

    for i in range(index, list_len):
        ans.append(input_list[i])
        recursive(i+1, level+1)
        ans.pop()


while True:
    input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if input_list[0] == 0:
        break
    k  = input_list[0]
    input_list = input_list[1:]
    list_len = len(input_list)
    ans = []
    recursive(0, 0)
    ans = []
    print()