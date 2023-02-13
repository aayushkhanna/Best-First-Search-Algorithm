from queue import PriorityQueue
v=14
graph = [[] for i in range(v)]

def bfs(source,target,n):
	visited = [0]*n
	visited[0] = True
	pq = PriorityQueue()
	pq.put((0,source))

	while pq.empty()==False:
		u = pq.get()[1]
		print(u,end = " ")
		if u == target:
			break
		for v,c in graph[u]:
			if visited[v] == False:
				visited[v] = True
				pq.put((c,v))
    print()


def addedge(x,y,cost):
	graph[x].append((y,cost))
	graph[y].append((x,cost))

addedge(0,1,3)
addedge(0,2,6)
addedge(0,3,5)
addedge(1,4,9)
addedge(1,5,8)
addedge(3,8,7)
addedge(8,10,6)
source=0
target=9
bfs(source,target,v)

