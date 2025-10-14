class Stack:
    def __init__(self):
        self.stack = []
    def Push(self,v):
        self.stack.append(v)
    def isempty(self):
        return(self.stack == [])
    def Pop(self):
        v = None
        if not self.isempty():
            v = self.stack.pop()
        return(v)    
    def __str__(self):
        return(str(self.stack))

# DFS Implementation for Adjacency list
def DFSList(AList,start_vertex):
    # Initializaion
    visited = {}
    for each_vertex in AList.keys():
        visited[each_vertex] = False    
    
    # Create stack object st
    st = Stack()
    
    # Push start_vertex in to the stack as first vertex
    st.Push(start_vertex)    
    
    # Repeat the following until the stack is empty
    while(not st.isempty()):
        # Pop one vertex from stack 
        current_vertex = st.Pop()
        # If popped vertex is not visited, marked visited
        if visited[current_vertex] == False:
            visited[current_vertex] = True
            # Push all unvisited adjacent of popped vertex into the stack
            for adj_veretx in AList[current_vertex]:
                 if(not visited[adj_veretx]):
                     st.Push(adj_veretx)    
    return(visited)


AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(DFSList(AList,0))