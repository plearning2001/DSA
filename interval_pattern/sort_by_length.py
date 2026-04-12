data = 10100
data = str(data)
data_map = set(data)
print(data_map)
print(len(data_map))
if '0' in data_map and '1' in data_map and len(data_map) == 2:
    print("true")
else:
    print("false")
