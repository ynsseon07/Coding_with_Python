# 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장

graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))

print(graph)