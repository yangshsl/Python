import queue
def bfs(graph, start):
    visited = {start}
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v=que.get()
        print(v, end='')
        nbr = graph[v]-visited
        for u in nbr:
            visited.add(u)
            que.put(u)