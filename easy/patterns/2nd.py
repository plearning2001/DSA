'''
1
12
123
1234
12345
'''

rows = 5
columns = 5

# --------------- Approach 1 ------------------ Simple nested loops
'''
for i in range(rows):
    counter = 1
    data = ""
    for j in range(i):
        data = data + str(counter)
        counter += 1
    print(data)

'''

# --------------- Approach 2 ------------------ Using end which decide what to do at end
'''
for i in range(rows):
    counter = 1
    data = ""
    for j in range(i):
        print(j+1, end="")
    print()
'''

# --------------- Approach 3 ------------------Memoization
data = ""
for i in range(rows):
    data = data + str(i+1)+" "
    print(data)
