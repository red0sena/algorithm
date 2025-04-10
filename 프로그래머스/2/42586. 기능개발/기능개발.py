from collections import deque
def solution(progresses, speeds):
    q = deque()
    for i in range(len(progresses)):
        a = ((100 - progresses[i]) // speeds[i])
        if ((100 - progresses[i]) % speeds[i]):
            a += 1
        q.append(a) 
    print(q)
    # 맨 처음 작업을 일단 뽑아옴
    before_time = q.popleft()
    count = 1
    answer = []
    while q:
        this_time = q.popleft()
        if before_time < this_time:
            answer.append(count)
            before_time = this_time
            count = 1
        else:
            count += 1
    answer.append(count)
    return answer