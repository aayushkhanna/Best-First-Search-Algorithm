from queue import PriorityQueue
v = 3
graph [(1,3),(2,6)],[(0,3)],[(0,6)],[(0,5),(8,7)],[(1,9)],[(1,8)],[(2,12)],[],[(3,7),(10,6)],[],[(8,6),(),[],[],[]]
def bfs(source,target,n):			
	visited = [0]*n
	visited[0] = True
	pq = PriorityQueue()
	pq.put((0,source))
	while pq.empty()==False:
		u = pq.get()[1]
	    print(u,end='')
	    if u==target:
	    	break
	    for v,c in graph[u]:
	    	if visited[v] == False:
	    		visited[v] = True
	    		pq.put((c,v))

    print()
source = 0
target = 10
bfs(source,target,v)


