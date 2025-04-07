
def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    ans = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            ans += 1
            right -= 1
            left += 1
        else:
            right -= 1
            ans += 1
    
    return ans
            