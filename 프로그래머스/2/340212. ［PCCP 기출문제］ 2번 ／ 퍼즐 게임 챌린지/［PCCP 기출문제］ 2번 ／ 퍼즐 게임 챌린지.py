def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    flag = False
    while left <= right:
        mid = (left + right) // 2
        takes_time = 0

        for i in range(len(diffs)):
            diff = diffs[i]
            if diff <= mid:
                takes_time += times[i]
            else:
                takes_time += (times[i-1] + times[i]) * (diff-mid) + times[i]

        if takes_time == limit:
            flag = True
            break
        elif takes_time > limit:
            left = mid + 1
        elif takes_time < limit:
            right = mid - 1


    if flag:
        return mid
    else:
        if left == mid:
            return mid
        else:
            return mid + 1