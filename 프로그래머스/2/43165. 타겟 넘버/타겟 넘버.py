
count = 0
def solution(numbers, target):
    n = len(numbers)

    def dfs(depth, sum_val):
        global count
        if n == depth:
            if sum_val == target:
                count += 1
            return

        dfs(depth + 1, sum_val + numbers[depth])
        dfs(depth + 1, sum_val - numbers[depth])

    dfs(0,0)
    return count