from collections import defaultdict

graph = defaultdict(lambda: [])
explored = {}
paths = 0


def DFS(start):
    global paths
    if explored.get(start, False):
        return
    if start == "end":
        paths += 1
        return
    if start.islower():
        explored[start] = True
    for neighbor in graph[start]:
        DFS(neighbor)
    explored[start] = False


try:
    while True:
        start, end = input().split("-")
        graph[start].append(end)
        graph[end].append(start)  # undirected graph
except EOFError:
    DFS("start")
    print(paths)
