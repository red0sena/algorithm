prefix = [0]
flag = True
for i in range(10):
    num = int(input())
    prefix_sum = prefix[i]+num
    if prefix_sum >= 100:
        if abs(prefix_sum - 100) > abs(100-prefix[i]):
            print(prefix[i])
        else:
            print(prefix_sum)
        flag = False
        break
    prefix.append(prefix_sum)

if flag:
    print(prefix[-1])