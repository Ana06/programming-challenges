from collections import defaultdict

graph = defaultdict(lambda: [])
explored = {}
paths = 0


def DFS(start, double=False):
    global paths
    double_current = False
    if start == "end":
        paths += 1
        return
    if start.islower():
        if explored.get(start, False):
            if double or start == "start":
                return
            else:
                double_current = True
                double = True
        explored[start] = True
    for neighbor in graph[start]:
        DFS(neighbor, double)
    if not double_current:
        explored[start] = False


try:
    while True:
        start, end = input().split("-")
        graph[start].append(end)
        graph[end].append(start)  # undirected graph
except EOFError:
    DFS("start", 0)
    print(paths)
