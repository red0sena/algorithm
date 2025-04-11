def solution(distance, rocks, n):
    rocks.sort()
    answer = 0

    left, right = 1, distance
    while left <= right:
        mid = (left+right) // 2
        count = 0
        prev = 0
        for rock_loc in rocks:
            diff = rock_loc - prev
            if diff < mid:
                count += 1
            else:
                prev = rock_loc
        
        if distance - prev < mid:
            count += 1
        if count <= n:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
        
    
    return answer