# isomorphic String 

s = "egg"
t = "add"

s = "badc"
t = "baba"

i = 0

dict = {}
isomorphic = True

while i < len(s):
    if s[i] in dict.keys():
        if dict[s[i]] != t[i]:
            isomorphic = False
            break
    else:
        dict[s[i]] = t[i]
    i += 1
values_len = len(set(dict.values()))
if values_len != len(dict.keys()):
    isomorphic = False

print(isomorphic)
