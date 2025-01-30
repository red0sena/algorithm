def solution(n, times):
    min_time = min(times)
    
    low, high = 0, min_time * n
    
    answer = high  
    
    while low <= high:
        mid = (low + high) // 2
        
        count = 0
        for t in times:
            count += mid // t
        if count >= n:
            answer = mid
            high = mid - 1
        else:

            low = mid + 1
    
    return answer
