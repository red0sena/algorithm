def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


def solution(sequence):
    prefix1 = [0]
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            prefix1.append(sequence[i])
        else:
            prefix1.append((-sequence[i]))
    a = (max_subarray_sum(prefix1))
    prefix2 = [0]
    
    for i in range(len(sequence)):
        if i % 2 != 0:
            prefix2.append(sequence[i])
        else:
            prefix2.append((-sequence[i]))
    b = (max_subarray_sum(prefix2))
    # print(prefix2, prefix1)
    return max(a,b)