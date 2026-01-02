# longest-substring-with-at-most-k-distinct-characters

from collections import Counter

letters = "aaaa"
k = 2
max_letters = 0

counter = Counter()
left = 0

for right in range(len(letters)):
    letter = letters[right]
    counter[letter] += 1

    while len(counter) > k:
        counter[letters[left]] -= 1
        if counter[letters[left]] == 0:
            del counter[letters[left]]
        left += 1

    max_letters = max(max_letters,right-left+1)

print(max_letters)
