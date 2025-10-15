def dijkstra(WMat,s):
    
    (rows,cols,x) = WMat.shape
    infinity = np.max(WMat)*rows+1
    (visited,distance) = ({},{})
    for v in range(rows):
        (visited[v],distance[v]) = (False,infinity)        
    distance[s] = 0
    
    
    for u in range(rows):
    
        min_dist = min([distance[v] for v in range(rows) if not visited[v]])
        print(f"min_dist -- {min_dist}")
        
    
        nextv_list = [v for v in range(rows)if (not visited[v]) and distance[v] == min_dist]
        print(f"nextv_list -- {nextv_list}")
        
    
        nextv = min(nextv_list)
        visited[nextv] = True
        
    
        for v in range(cols):            
            if WMat[nextv,v,0] == 1 and (not visited[v]):
                #If distance of v through nextv is smaller than the current distance on v, then update
                if distance[nextv] + WMat[nextv,v,1] < distance[v]:
                    distance[v] = distance[nextv] + WMat[nextv,v,1]
    return(distance)



dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7
import numpy as np
W = np.zeros(shape=(size,size,2))
for (i,j,w) in dedges:
    W[i,j,0] = 1
    W[i,j,1] = w
print(f"Initial matrix -- {W}")
print(dijkstra(W,0))