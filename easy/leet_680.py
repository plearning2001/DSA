def check_palindrome(a,b,data):
    while a <=b:
        if data[a] == data[b]:
            a += 1
            b -= 1
        else:
            return False
    return True



s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
i = 0
j = len(s)-1
is_palindrome = True
chances = True

while i<=j:
    if s[i] == s[j]:
        print(s[i])
        i += 1
        j -= 1
    else:
        if check_palindrome(i,j-1,s) or check_palindrome(i+1,j,s):
            return True
        else:
            return False

        
print(is_palindrome)