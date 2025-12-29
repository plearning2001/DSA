s = "  the  sky  is  blue  "
b = []
l = 0
r = len(s)-1

while l <= r:
    if s[l] == " ":
        l += 1
    else:
        break

while r <= 0:
    if s[r] == " ":
        r -= 1
    else:
        break
lett_list = []

for k in range(l,r-1):
    if s[k] == " ":
        if s[k-1] == " ":
            continue
        else:
            lett_list.append(s[k])
    else:
        lett_list.append(s[k])


print(lett_list)

n = 0
m = len(lett_list)-1
while n <= m:
    lett_list[n],lett_list[m] = lett_list[m],lett_list[n]
    n += 1
    m -= 1
print(lett_list)