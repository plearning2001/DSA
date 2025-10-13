
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

# Using BFS approch For Adjacency list, for path, maintaining the parent of each vertex
# Using BFS approch maintaing the adjacent level number from source vertrex
def BFSListPathLevel(AList,v):
    # Initialization
    (level,parent) = ({},{})
    for each_vertex in AList.keys():
        level[each_vertex] = -1
        parent[each_vertex] = -1
    
    # Create Queue object q
    q = Queue()
    
    # Assigning the level 0 for start_vertex and insert it into the queue
    level[v] = 0
    q.enqueue(v)
    
    # Repeat the following until the queue is empty
    while(not q.isempty()):
        # Remove the one vertex from queue
        curr_vertex = q.dequeue()
        # Visit the each adjacent of curr_vertex(if level value is -1) and insert into the queue
        for adj_vertex in AList[curr_vertex]:
            if (level[adj_vertex] == -1):
                # Assign the level value on each adjacent one more than the curr_vertex level
                level[adj_vertex] = level[curr_vertex] + 1
                # Assigne the curr_vertex as parent of adjacent vertex of curr_vertex
                parent[adj_vertex] = curr_vertex
                q.enqueue(adj_vertex)
                
    return(level,parent)


AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(BFSListPathLevel(AList,0))