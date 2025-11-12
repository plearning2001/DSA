'''
*****
****
***
**
*
'''
rows = 5
columns = 5
# --------------- Approach 2 ------------------ Using single reverse loop
'''
for i in range(rows,0,-1):
    print("* "*i)
'''

# --------------- Approach 2 ------------------ Using formula
'''
for i in range(rows):
    print("*"*(columns+1 - i))
'''

# --------------- Approach 3 ------------------Memoization
