import sys


num = "1221000"
left = 0
right = 2

first = num[0]
second = num[1]
third = num[2]
highest = -sys.maxsize

my_map = set([first,second,third])


for right in range(2,len(num)):
    if len(set(num[left:right+1])) == 1 and int(str(num[right])*3) > int(highest):
        highest = str(num[right])*3

    left += 1

print(highest)