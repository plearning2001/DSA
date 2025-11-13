'''
    *
   ***
  *****
 *******
*********
'''

rows = 5
colunms = 5
# --------------- Approach 1 ------------------ Using formula
for i in range(rows):
    data = " "*(colunms+1-i)
    print(f"{data}{"*"*(2*i + 1)}")