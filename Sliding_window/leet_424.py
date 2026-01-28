s = "AABABBA"
k = 2

left = 0
freq = {}
max_lenth = 0
max_freq = 0

for right in range(len(s)):
    char = s[right]
    freq[char] = freq.get(char,0) + 1
    max_freq = max(max_freq,freq[char])

    while (right-left+1) - max_freq > k:
        freq[s[left]] -= 1
        left += 1

    max_lenth = max(max_lenth,right-left+1)
print(max_lenth)