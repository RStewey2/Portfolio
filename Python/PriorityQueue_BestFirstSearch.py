from queue import PriorityQueue

v = 9

graph = [[] for i in range(v)] 
 
def best_first_search(source, goal, n):
    visited = [False] * n
    visited = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        print(u, end=" ")
        if u == goal:
            break
 
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()
  
 
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
 
 
addedge(0, 1, 35)
addedge(0, 2, 90)
addedge(0, 3, 62)
addedge(0, 4, 75)
addedge(0, 5, 80)
addedge(0, 6, 43)
addedge(0, 7, 1000)
addedge(1, 0, 35)
addedge(1, 2, 50)
addedge(1, 3, 28)
addedge(1, 4, 54)
addedge(1, 5, 97)
addedge(1, 6, 82)
addedge(1, 7, 700)
addedge(2, 0, 90)
addedge(2, 1, 50)
addedge(2, 3, 78)
addedge(2, 4, 55)
addedge(2, 5, 10)
addedge(2, 6, 21)
addedge(2, 7, 600)
addedge(3, 0, 62)
addedge(3, 1, 28)
addedge(3, 2, 78)
addedge(3, 4, 67)
addedge(3, 5, 83)
addedge(3, 6, 49)
addedge(3, 7, 500)
addedge(4, 0, 75)
addedge(4, 1, 54)
addedge(4, 2, 55)
addedge(4, 3, 67)
addedge(4, 5, 17)
addedge(4, 6, 20)
addedge(4, 7, 400)
addedge(5, 0, 80)
addedge(5, 1, 97)
addedge(5, 2, 10)
addedge(5, 3, 83)
addedge(5, 4, 17)
addedge(5, 6, 99)
addedge(5, 7, 300)
addedge(6, 0, 43)
addedge(6, 1, 82)
addedge(6, 2, 21)
addedge(6, 3, 49)
addedge(6, 4, 20)
addedge(6, 5, 99)
addedge(6, 7, 25)
addedge(7, 0, 29)
addedge(7, 1, 22)
addedge(7, 2, 79)
addedge(7, 3, 25)
addedge(7, 4, 74)
addedge(7, 5, 55)
addedge(7, 6, 25)
addedge(7, 8, 91)
addedge(8, 7, 91)

source = 0
goal = 8
best_first_search(source, goal, v)