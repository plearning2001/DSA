import sys


num = "1221000"
i = 0
first = num[0]
second = num[1]
third = num[2]
highest = -sys.maxsize

if first == second == third:
    if int(first+second+third) > int(highest):
        highest = first+second+third
while i <= len(num)-3:
    first = num[i]
    second = num[i+1]
    third = num[i+2]

    if first == second == third:
        if int(first+second+third) > int(highest):
            highest = first+second+third

    i += 1
if highest == -sys.maxsize:
    print("")
print(highest)