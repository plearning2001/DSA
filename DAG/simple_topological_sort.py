# Implementaion of Queue
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

# Implementation of Topological sort for Adjacency list
def toposortlist(AList):
    # Initialization
    (indegree,toposortlist) = ({},[])
    zerodegreeq = Queue()
    for u in AList.keys():
        indegree[u] = 0
    
    # Compute indegree for each vertex
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    
    # Find the vertex with indegree 0 and added into the queue
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.enqueue(u)
    
    # Topological sort Computing process
    while (not zerodegreeq.isempty()):
        # Remove one vertex from queue which have zero degree vertices
        curr_vertex = zerodegreeq.dequeue()       
        # Store the removed vertex in toposortlist and reduce the indegree by one 
        toposortlist.append(curr_vertex)
        indegree[curr_vertex] = indegree[curr_vertex]-1
        
        # Repeat for each adjacent of the removed vertex
        for adj_vertex in AList[curr_vertex]:
            # Reduce the indegree of each adjacent of the removed vertex by 1
            indegree[adj_vertex] = indegree[adj_vertex] - 1
            # If after reducing the degree of adjacent, it becomes zero then insert it into the queue
            if indegree[adj_vertex] == 0:
                zerodegreeq.enqueue(adj_vertex)                
    
    return(toposortlist)

AList={0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(toposortlist(AList))