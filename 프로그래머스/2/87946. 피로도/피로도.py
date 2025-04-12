def solution(k, dungeons):
    
    def recursive(input_list, now_k, count):
        if not input_list:
            return count
        count_list = [count]
        for i in range(len(input_list)):
            if input_list[i][0] <= now_k:
                count_list.append(recursive(input_list[:i]+input_list[i+1:], now_k-input_list[i][1], count+1))
        
        max_count = max(count_list)
        
        return max_count
    
    answer = recursive(dungeons, k, 0)
    
                
    return answer