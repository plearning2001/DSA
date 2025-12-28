a = [4,9,5]
b = [9,4,9,8,4]
return_list = []
i = 0
j = 0

while i< len(a) and j< len(b):
    if a[i]<b[j]:
        i += 1
    elif a[i]>b[j]:
        j += 1
    else:
        return_list.append(a[i])
        i += 1
        j += 1
    
    print(f"outpur -- {return_list}")