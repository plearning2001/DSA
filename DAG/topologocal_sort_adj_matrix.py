# Implementation of Topological sort for Adjacency matrix
def toposort(AMat):
    #Initialization
    (rows,cols) = AMat.shape
    indegree = {}
    toposortlist = []
    
    #Compute indegree for each vertex
    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if AMat[r,c] == 1:
                indegree[c] = indegree[c] + 1
    print(f"base -- indegree {indegree}")



    # Topological sort Computing process
    for i in range(rows):
        # Select the min level vertex for removing the graph which has indegree 0
        j = min([k for k in range(cols) if indegree[k] == 0])
        print(f"j -- {j}")
        # Store the removed vertex j in toposortlist and reduce the indegree by one 
        toposortlist.append(j)
        indegree[j] = indegree[j] - 1
        
        # Reduce the indegree of each adjacent of the removed vertex j by 1
        for k in range(cols):
            if AMat[j,k] == 1:
                indegree[k] = indegree[k] - 1
                
    return(toposortlist)


edges=[(0,2),(0,3),(0,4),(1,2),(1,7),(2,5),(3,5),(3,7),(4,7),(5,6),(6,7)]
size = 8
import numpy as np
AMat = np.zeros(shape=(size,size))
print(f"Input AMAT -- \n {AMat}")
for (i,j) in edges:
    AMat[i,j] = 1
print(f"Input AMAT with edges -- \n {AMat}")    
print(toposort(AMat))