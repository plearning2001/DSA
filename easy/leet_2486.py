s = "abcde"
t = "a"

i = 0
j = 0
# count = 0

while i < len(s) and j < len(t):
    if t[j] == s[i]:
        # count += 1
        i += 1
        j += 1
    else:
        i += 1

print(len(t)-j)