from collections import deque

graph = {'1': ['2', '3'],
         '2': ['4', '5'],
         '3': ['1'],
         '4': ['2'],
         '5': ['2'],
         '6': ['3']}


def bfs(graph, start, search):
    searchQueue = deque()
    searchQueue += graph[start]
    visited = []
    while searchQueue:
        node = searchQueue.popleft()
        if node not in visited:
            if node == search:
                print('Found')
                print(visited)
                return True
            else:
                searchQueue += graph[node]
                visited += [node]
    print('not found')
    return False


bfs(graph, input('Начальная точка '), input('Искомая точка '))
