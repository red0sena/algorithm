def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + triangle[i][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])

    return(max(triangle[-1]))