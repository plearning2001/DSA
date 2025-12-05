a = [1,2,3,4,5,6,7,8,9]
b = [2,3,4,5,11]

#target = [1,2,3,4,5,6]

c = []

i=0
j=0
len_a = len(a)
len_b = len(b)

while i<len_a or j<len_b:
    if i>=len_a:
        c.append(b[j])
        j+=1
        continue
    if j>=len_b:
        c.append(b[i])
        i+=1
        continue    

    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    elif a[i]>b[j]:
        c.append(b[j])
        j+=1
    
    
    #Remove duplicates
    else:
        c.append(b[j])
        j+=1
        i+=1

print(c)