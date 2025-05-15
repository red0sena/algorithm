def solution(babbling):
    count = 0
    word4 = set(["aya", "ye", "woo", "ma"])

    for word in babbling:
        n = len(word)
        start =  0
        flag = True
        while start < n:
            if word[start:start+2] in word4:
                start += 2
            elif word[start:start+3] in word4:
                start += 3
            else:
                flag = False
                break
        if flag:
            count += 1

    return count