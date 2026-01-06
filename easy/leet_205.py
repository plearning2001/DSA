# isomorphic String 


s = "foo"
t = "bar"

s = "badc"
t = "baba"

s = "egg"
t = "add"

i = 0
s_set = set()
t_set = set()
isomorphic = True

while i < len(s):
    s_set.add(s[i])
    t_set.add(t[i])
    i += 1
if len(s_set) != len(t_set):
    isomorphic = False
print(isomorphic)



# dict = {}
# isomorphic = True

# while i < len(s):
#     if s[i] in dict.keys():
#         if dict[s[i]] != t[i]:
#             isomorphic = False
#             break
#     else:
#         dict[s[i]] = t[i]
#     i += 1
# values_len = len(set(dict.values()))
# if values_len != len(dict.keys()):
#     isomorphic = False

# print(isomorphic)
