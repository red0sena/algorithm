

def dfs(result, target, idx, numbers, count):
    if len(numbers) == idx:
        if result == target:
            count += 1
        return count
    else:
        count = dfs(result+numbers[idx], target, idx+1, numbers, count)
        count = dfs(result-numbers[idx], target, idx+1, numbers, count)
    
    return count


def solution(numbers, target):
    answer = dfs(0, target, 0, numbers, 0)
    return answer