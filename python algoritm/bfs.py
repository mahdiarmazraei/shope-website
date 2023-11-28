#____________bfs_____________
def bfs(visit, graph, nodes):
    y = []
    for node in nodes:
        if node not in visit:
            print(node)
            visit.add(node)
            print(visit)
            y += graph[node]
    while len(visit) != len(graph):
         bfs(visit, graph, y)

graph = {
    'a':['b', 'c', 'd'],
    'b':['a', 'e', 'd'],
    'c':['a', 'd'],
    'd':['a', 'b', 'c', 'e'],
    'e':['b', 'd'],
}
a = ['a']
x = set()
bfs(x, graph, a)