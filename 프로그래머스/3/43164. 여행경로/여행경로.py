

def solution(tickets):  
    n = len(tickets)
    visited = [-1] * n


    sort_list = []

    def dfs(ticket, list_res):
        if n+1 == len(list_res):
            sort_list.append([*list_res])
            return
        for i in range(n):
            if tickets[i][0] == ticket and visited[i] == -1:
                visited[i] = 1
                list_res.append(tickets[i][1])
                dfs(tickets[i][1], list_res)
                list_res.pop()
                visited[i] = -1



    dfs("ICN", ["ICN"])
    sort_list.sort()
    return sort_list[0]