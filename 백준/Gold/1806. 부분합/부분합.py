n, s = map(int, input().split())

input_list = list(map(int, input().split()))



start, end, current_val = 0, 0, 0
min_len = 100000001

while True:
    if current_val < s and end < n:
        current_val += input_list[end]
        end += 1
    elif current_val >= s:
        min_len  = min(min_len, end-start)
        current_val -= input_list[start]
        start += 1
    else:
        break

if min_len == 100000001:
    print(0)
else:
    print(min_len)