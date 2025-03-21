def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], arr[i]+current_sum)
        max_sum = max(max_sum, current_sum)
    print(max_sum)
    return max_sum
def solution(sequence):
    pers1_sequence = []
    pers2_sequence = []
    for i in range(len(sequence)):
        if i % 2 == 0:
            pers1_sequence.append(-sequence[i])
            pers2_sequence.append(sequence[i])
        else:
            pers1_sequence.append(sequence[i])
            pers2_sequence.append(-sequence[i])
    
    pers1 = max_subarray_sum(pers1_sequence)
    pers2 = max_subarray_sum(pers2_sequence)
            
            
    return max(pers1, pers2) 