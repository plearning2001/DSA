nums = [-1,0,3,5,9,12]
target = 9


left = 0
data = nums
right = len(data) - 1
        

while left <= right:
    middle = (left + right)//2
    if data[middle] == target:
        print(middle)
    else:
        if target > data[middle]:
            left = middle+1
        else:
            right = middle-1
if target == data[right]:
    print (right)

print -1