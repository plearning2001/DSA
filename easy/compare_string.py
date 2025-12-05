str1 = " abc"
str2 = "d b c"

i = 0
j = 0

while i < len(str1) and j < len(str2):
    if str1[i] == " ":
        i += 1
        continue
    if str2[j] == " ":
        j += 1
        continue
    if str1[i] == str2[j]:
        i += 1
        j += 1
        continue
    else:
        print("false")
        break
print("true")