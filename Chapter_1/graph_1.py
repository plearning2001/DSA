import numpy as np
# Given vertices and edges
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] # each tuple(u,v) represent edge from u to v

size = len(V)
print(f"size of graph -- {size}")

AMat = np.zeros(shape=(size,size))
print(f"graph of zeros -- {AMat}")

for i,j in E:
  print(f"{i} - {j}")
  print(f"test -- {AMat[i,j]}")
  AMat[i,j] = 1

print(f"sgraph with values -- {AMat}")