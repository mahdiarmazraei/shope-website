#______________dfs_____________
def dfs(node, visit, gragh ):
    # print(visit)
    if node not in visit:
        print(node)
        visit.add(node)
        print(visit,"*")
        for i in gragh[node]:
            print(visit,'1')
            dfs(i, visit, gragh)
            print(visit,'2')


gragh = {
    'a':['b', 'c', 'd'],
    'b':['a', 'e', 'd'],
    'c':['a', 'd'],
    'd':['a', 'b', 'c', 'e'],
    'e':['b', 'd'],
}
visit = set()
dfs('a',visit, gragh)

