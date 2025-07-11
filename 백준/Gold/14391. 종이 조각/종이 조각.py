def solution():
    # Read input
    N, M = map(int, input().split())
    paper = [list(map(int, input().strip())) for _ in range(N)]
    
    # dp[mask] represents max sum for the configuration represented by mask
    dp = {}
    
    def get_number(x, y, dx, dy, length):
        """Calculate number formed by a piece starting at (x,y) in direction (dx,dy)"""
        num = 0
        for _ in range(length):
            num = num * 10 + paper[x][y]
            x, y = x + dx, y + dy
        return num
    
    def solve(mask, pos):
        if pos == N * M:
            return 0
        if (mask, pos) in dp:
            return dp[(mask, pos)]
        
        max_sum = 0
        row, col = divmod(pos, M)
        
        # Skip if position is already used
        if mask & (1 << pos):
            return solve(mask, pos + 1)
        
        # Try horizontal pieces of different lengths
        for length in range(1, M - col + 1):
            # Check if all positions in this horizontal piece are free
            valid = True
            new_mask = mask
            for j in range(length):
                if mask & (1 << (pos + j)):
                    valid = False
                    break
                new_mask |= (1 << (pos + j))
            
            if valid:
                num = get_number(row, col, 0, 1, length)
                max_sum = max(max_sum, num + solve(new_mask, pos + length))
        
        # Try vertical pieces of different lengths
        for length in range(1, N - row + 1):
            # Check if all positions in this vertical piece are free
            valid = True
            new_mask = mask
            for i in range(length):
                if mask & (1 << (pos + i * M)):
                    valid = False
                    break
                new_mask |= (1 << (pos + i * M))
            
            if valid:
                num = get_number(row, col, 1, 0, length)
                max_sum = max(max_sum, num + solve(new_mask, pos + 1))
        
        dp[(mask, pos)] = max_sum
        return max_sum
    
    return solve(0, 0)

# Run the solution and print result
print(solution())