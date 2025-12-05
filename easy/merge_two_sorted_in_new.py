a = [1,2,2,3,4,5,6,7,8,9]
b = [2,3,4,5,11]
print(f"a - {a} \n b - {b}")

#target = [1,2,3,4,5,6]

c = []

i=0
j=0
len_a = len(a)
len_b = len(b)

def add_element(c,element):
    if element in c:
        return
    else:
        c.append(element)

while i<len_a or j<len_b:
    if i>=len_a:
        add_element(c,b[j])
        j+=1
        continue
    if j>=len_b:
        add_element(c,b[i])
        i+=1
        continue    

    if a[i]<b[j]:
        add_element(c,a[i])
        i+=1
    elif a[i]>b[j]:
        add_element(c,b[j])
        j+=1
    
    
    #Remove duplicates
    else:
        add_element(c,b[j])
        j+=1
        i+=1

print(c)