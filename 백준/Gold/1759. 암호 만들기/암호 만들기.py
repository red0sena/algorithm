import sys


l, c = map(int, sys.stdin.readline().rstrip().split(" "))
char_list = sorted(sys.stdin.readline().rstrip().split(" "))
list_len = len(char_list)
ans = []

def recursive(index, level):
    if level == l:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        if not vowels.intersection(ans):
            return
        result = [char for char in ans if char not in vowels]
        if len(result) < 2:
            return
        for i in ans:
            print(i, end = "")
        print()
        return

    for i in range(index, list_len):
        ans.append(char_list[i])
        recursive(i+1, level+1)
        ans.pop()

recursive(0, 0)
