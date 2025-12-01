# data = [ 0,1,1,0,1,0,2,0,1]
data =[0,1,0,3,12]
# output -  [1,1,1,2,1,0,0,0,0]
i = 0
j = 0

while j < len(data):
    if data[j] != 0:
        data[i],data[j] = data[j], data[i]
        i += 1
        j += 1
    else:
        j += 1


print(data)
