'''
s = 101010
data = str(s)
for i in data:
      if i !=1 and i != 0:
            print(False)

print(True)

'''

data = 2323
data = str(data)
data_map = set(data)
print(data_map)
print(len(data_map))
if '0' in data_map and '1' in data_map and len(data_map) == 2:
    print("true")
else:
    print("false")
