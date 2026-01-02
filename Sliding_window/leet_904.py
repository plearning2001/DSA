# fruit-into-baskets

from collections import Counter

fruits = [2,1,2,3,2,2]
k = 2
max_fruits = 0

counter = Counter()
left = 0

for right in range(len(fruits)):
    fruit = fruits[right]
    counter[fruit] += 1

    while len(counter) > k:
        counter[fruits[left]] -= 1
        if counter[fruits[left]] == 0:
            del counter[fruits[left]]
        left += 1

    max_fruits = max(max_fruits,right-left+1)

print(max_fruits)
