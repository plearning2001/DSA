from collections import deque

class Stack:

    def __init__(self):
        self.Q = deque()

    def pop(self):
        return self.Q.pop()

    def push(self, x):
        return self.Q.append(x)

    def isempty(self):
        return False if self.Q else True





def CheckConnectivity(adj_dict,exc_camp):
    all_vertices = [v for v in adj_dict.keys() if v != exc_camp]
    if not all_vertices:
        return True
    print(f"all_vertices -- {all_vertices}")

    visited = {}
    for i in all_vertices:
        visited[i] = False

    st = Stack()
    st.push(all_vertices[0])

    while not st.isempty():
        vertex = st.pop()
        if vertex!= exc_camp and not visited[vertex]:
            print(vertex)
            visited[vertex] = True
            for neighbor in adj_dict[vertex]:
                print(f"neighbor -- {neighbor}")
                st.push(neighbor[0])
    print(f"After visiting -- {visited}")

    return all(value for value in visited.values())



def MST(adj_dict,exc_camp):
    # first check if all are connected or not
    if not CheckConnectivity(adj_dict,exc_camp):
        return -1
    
    print("Yess")
    print(f"adj_dict -- {adj_dict}")
    edges = []
    components, members, size = {},{},{}
    min_cost = 0
    te = []
    
    for u in adj_dict.keys():
        if u != exc_camp:
            edges.extend([(d,u,v) for v,d in adj_dict[u] if v!= exc_camp ])
            print(f"edges -- {edges}")

            components[u],members[u],size[u] = u,[u],1
    # We need to sort by distance, that's why distance is at first in tuple
    edges.sort()

    distinctEdges = [edges[0]]
    print(f"distinctEdges -- {distinctEdges}")
    for i in range(len(edges) - 1):
        if not ((edges[i][0] == edges[i + 1][0]) and edges[i][1]
                == edges[i + 1][2] and edges[i][2] == edges[i + 1][1]):
            distinctEdges.append(edges[i + 1])
    edges = distinctEdges
    print(f"distinctEdges -- {distinctEdges}")

    # Kruskal
    print(f"members -- {members}\n")
    for p,q,r in edges:
        if components[q] != components[r]:
            te.append((q,r))
            min_cost += p
            # Create group of old members
            # Then add it in new group
            # And update their components

            c_old = components[q]
            c_new = components[r]
            for m in members[c_old]:
                components[m] = c_new
                members[c_new].append(m)
                size[c_new] += 1
    
                print(f"components -- {components}")
                print(f"members -- {members}\n")
    return min_cost

# inputs
camps_list = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
n = 7 #no. of camps
ex_camp = 4 #Excluded camp

adj_dict = {i:[] for i in range(n)}
print(f"adj_dict -- {adj_dict}")

# for undirected graph
for j,k,l in camps_list:
    adj_dict[j].append((k,l))
    adj_dict[k].append((j,l))

# result = MST(adj_dict,ex_camp)
result = MST(adj_dict,ex_camp)
print(f"Final result -- {result}")