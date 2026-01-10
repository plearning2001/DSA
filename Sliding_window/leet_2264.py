import sys


num = "1221000"
left = 0
highest = -sys.maxsize

for right in range(2,len(num)):
    if len(set(num[left:right+1])) == 1 and int(str(num[right])*3) > int(highest):
        highest = str(num[right])*3

    left += 1

print(highest)

# ###########################################

left = 0
highest = -sys.maxsize

for right in range(2,len(num)):
    if num[right] == num[right-1] == num[right-2]:
        highest = str(num[right])*3

    left += 1

print(highest)