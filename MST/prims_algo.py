def prims_algo(WList):
    # Initialization
    infinity = 1 + max([d for u in WList.keys() for (v,d) in WList[u]])
    (visited,distance,TreeEdges) = ({},{},[])
    for v in WList.keys():
        (visited[v],distance[v]) = (False,infinity)
    
    # Start from vertex 0, marked visited and update the distance of adjacents from 0
    print(f"start distance -- {distance}")
    visited[0] = True
    print(f"visited -- {visited}\n")
    for (v,d) in WList[0]:
        print(f"start -- {WList[0]}")
        print(f"--- {v,d}")
        distance[v] = d
    print(f"modified distance -- {distance}")

    print(f"disance -- {distance} \n\n")
   
    # Repeat the below process (number of vertices-1) times
    for i in range(1,len(WList.keys())):  
        print(f"\n first loop i--- {i}")
        mindist = infinity
        nextv = None
        print(f"mindist -- {mindist}")
        print(f"nextv -- {nextv}")

        #Finding the minimum weight edge (u,v) where vertex u is visited and v is not visited 
        for u in WList.keys():
            print(f"\n second loop i--- {u}")
            for (v,d) in WList[u]:
                print(f"vd -- {(v,d)}")
                if visited[u] and (not visited[v]) and d < mindist:
                    mindist = d
                    nextv = v
                    nexte = (u,v)
                    print(f"mindist -- {mindist}")
                    print(f"nextv -- {nextv}")
                    print(f"nexte -- {nexte}")
        
        # Mark nextv as visited and append the nexte in MST
        visited[nextv] = True
        TreeEdges.append(nexte)
        
        # Update the distance of unvisited adjacents of nextv if smaller than current
        for (v,d) in WList[nextv]:
            if not visited[v]:
                if d < distance[v]:
                    distance[v] = d
        print(f"visited at end -- {visited}")
        print(f"distance at end -- {distance}")
    return(TreeEdges)


dedges = [(0,1,10),(0,3,18),(1,2,20),(1,3,6),(2,4,8),(3,4,70)]
edges = dedges + [(j,i,w) for (i,j,w) in dedges]
size = 5
WL = {}
for i in range(size):
    WL[i] = []
for (i,j,d) in edges:
    WL[i].append((j,d))
print(WL)
print(prims_algo(WL))