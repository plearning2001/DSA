a = 6
b = 20
counter = max(a,b)
interval = max(a,b)
lcm = 0
while True:
    if counter%a == 0 and counter%b == 0:
        lcm = counter
        break
    counter += interval
print(lcm)