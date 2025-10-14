# Setting all vertices visited false and parent -1
def DFSInitList(AList):
    (visited,parent) = ({},{})
    for each_vertex in AList.keys():
        visited[each_vertex] = False
        parent[each_vertex] = -1
    return(visited,parent)



def DFSList(AList,v,p,curr_v):

    curr_vertex = AList[curr_v]
    print(f"current_v -- {curr_v}")
    v[curr_v] = True

    adj_v = AList[curr_v]
    for i in adj_v:
      if (not v[i]):
        p[i] = curr_v

        DFSList(AList,v,p,i)
    return(v,p)







AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
v,p = DFSInitList(AList)
print(DFSList(AList,v,p,0))