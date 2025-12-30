data = [100,700,300,400]
k = 2

max_total = 0
sum = 0
for i in range(0,k):
    sum = sum + data[i]
    if sum > max_total:
        max_total = sum

for j in range(k,len(data)):
    sum = sum + data[j]
    sum = sum - data[j-k]

    if sum > max_total:
        max_total = sum

print(max_total)