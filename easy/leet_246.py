# strobogrammatic number

number = "1988612"
dict = {
    "8":"8",
    "6":"9",
    "1":"1",
    "9":"6",
    "0":"0"
}

i = 0
j = len(number)-1
flag = True

while i<=j:
    if number[i] not in dict.keys() or number[j] != dict[number[i]]:
        flag = False
        break
    else:
        i += 1
        j -= 1

print(flag)