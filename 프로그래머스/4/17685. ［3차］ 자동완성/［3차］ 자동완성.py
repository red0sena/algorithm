import sys
from collections import defaultdict

def solution(words):
    # Trie 노드: {char: [children_dict, count]}
    # 간단하게 dict of dict로 구현
    trie = {}
    
    # Trie 삽입
    for word in words:
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = [dict(), 0]
            node[ch][1] += 1  # 이 노드를 지나는 단어 수 증가
            node = node[ch][0]
    
    # 각 단어별 필요한 입력 수 계산
    answer = 0
    for word in words:
        node = trie
        for i, ch in enumerate(word):
            if node[ch][1] == 1:
                # 이 노드에서 유일 → i+1 글자만 입력하면 됨
                answer += i + 1
                break
            node = node[ch][0]
        else:
            # 끝까지 count > 1 이었으면 단어 전체 입력
            answer += len(word)
    
    return answer