# longest-substring-without-repeating-characters

s = "abcbbcbb"

i = 0
j = 0
char_set = set()
max_total = 0

while j < len(s):
    c = s[j]

    while c in char_set:
        #Keep removing from left
        char_set.remove(s[i])
        i += 1
    
    char_set.add(c)
    # compare with max and current window length
    max_total = max(max_total,j-i+1)
    j += 1
print(max_total)