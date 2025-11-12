'''
12345
1234
123
12
1
'''

rows = 5
colunms = 5
# --------------- Approach 1 ------------------ Using single reverse loop

for i in range(rows,0,-1):
    for j in range(i):
        print(j+1, end="")
    print()
