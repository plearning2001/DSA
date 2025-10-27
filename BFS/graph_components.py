# Components of vertex in multi component graph

# Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,v):
        self.queue.append(v)
    def isempty(self):
        return(self.queue == [])
    def dequeue(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)    
    def __str__(self):
        return(str(self.queue))

# BFS Implementation for Adjacency list
def BFSList(AList,start_vertex):
    visited = {}
    for each_vertex in AList.keys():
        visited[each_vertex] = False
    
    q = Queue()    
    visited[start_vertex] = True
    visited[4] = True
    q.enqueue(start_vertex)
    
    while(not q.isempty()):
        curr_vertex = q.dequeue()
        for adj_vertex in AList[curr_vertex]:
            if (not visited[adj_vertex]):
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)               
    return(visited)

# Implementation to find connected components in graph
def Components(AList):
    # Initialization of component value -1 for each vertex
    component = {}
    for each_vertex in AList.keys():
        component[each_vertex] = -1   
    
    # Initialize compid(represent conntected component id)
    # Initialize seen(represent number of visited/checked vertices)
    (compid,seen) = (0,0)
    
    # Repeat the following untill seen value is not equal to number of vertex
    while seen < max(AList.keys()):
        # Find the min level value vertex among all vertices which are not checked or visited
        startv = min([i for i in AList.keys() if component[i] == -1])
        # Call the BFS to check the reachability from startv
        visited = BFSList(AList,startv)  
        print(f"visited -- {visited}")
        # Assign compid value to each reachable vertex from startv and increment seen value
        for vertex in visited.keys():
            if visited[vertex]:
                seen = seen + 1
                component[vertex] = compid
        
        # Increment compid by one to check again if any vertex are remaing to visisted 
        compid = compid + 1
        print(f"compid -- {compid}")
    
    return(component)


# AList = {0: [1], 1: [2], 2: [0], 3: [4, 6], 4: [3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
AList = {0: [1,2,3], 5: [6], 2: [1,5,4], 6: [4], 1: [6,3], 3: [4]}

print(Components(AList))