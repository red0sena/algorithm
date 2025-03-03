import math

n = int(input())
input_list = list(map(int, input().split()))

res = -int(10e10)


window_size = n - (4-1)


for i in range(0, n-window_size+1):
    a = math.prod(input_list[i:i+window_size])

    b = sum(input_list[:i])
    c = sum(input_list[i+window_size:])
    res = max(res, a+b+c)




print(res)