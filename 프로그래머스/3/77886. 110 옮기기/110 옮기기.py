def solution(s):
    ans = []
    for string in s:
        stack = []
        count_110 = 0
        for char in string:
            stack.append(char)
            if stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count_110 += 1
        remain_str = ''.join(stack)
        pos = remain_str.rfind('0')
        if pos == -1:
            res = "110" * count_110 + remain_str
        else:
            res = remain_str[:pos+1] + ("110" * count_110) + remain_str[pos+1:]
            
        ans.append(res)
    return ans