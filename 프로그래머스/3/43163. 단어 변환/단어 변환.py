min_res = 10e9

def solution(begin, target, words):
    global min_res
    n = len(words)
    words_len = len(words[0])
    visited = []

    def dfs(depth, now_word):
        global min_res
        if now_word == target:
            min_res = min(depth, min_res)
            return

        for i in range(words_len):
            for word in words:
                if (word[:i]+word[i+1:]) == (now_word[:i]+now_word[i+1:]) and not word in visited:
                    visited.append(word)
                    dfs(depth+1, word)
                    visited.pop()

    dfs(0, begin)
    if min_res > 51:
        min_res = 0
    return min_res