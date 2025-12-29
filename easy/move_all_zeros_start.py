data = [0,1,1,1,0,0,1,1]
i = 0
j = len(data)-1

while i<j:
    if data[i] == 0:
        i += 1
    elif data[j] == 1:
        j -= 1
    else:
        data[i],data[j] = data[j], data[i]
        j -= 1
        i == 1

print(data)


