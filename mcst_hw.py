



camps_list = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
adj_list = {}
for l,m,n in camps_list:
    adj_list[l] = []

for l,m,n in camps_list:
    adj_list[l].append((m,n))

for key in adj_list:
    print(f"adj_list -- {key} -- {adj_list[key]}")

infinity = 1 + max([d for u in adj_list.keys() for (v,d) in adj_list[u]])

print(infinity)

distance = {}
visited = {}
edges = []
for i in adj_list:
    distance[i],visited[i] = infinity,0
print(f"distance -- {distance} {visited}")

visited[0] = True
for i in range(1,len(adj_list.keys())):
    min_dist = infinity
    nextv = None

    for k in adj_list.keys():
        for v,d in adj_list[k]:
            if visited[k] and (not visited[v] and d < min_dist):
                min_dist = d
                nextv = v
                nexte = (k,v)
        visited[k] = 1
        neighbors = adj_list[k]
        print(f"neighbors -- {neighbors}")

    visited[nextv] = True
    edges.append(nexte)

print(f"Edges -- {edges}")