# max-consecutive-ones

nums = [0,0,0,0]
k = 0

# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3


left = 0

freq = 0
max_len = 0
answer = 0

for right in range(len(nums)):
    if nums[right] == 1:
        freq += 1

    max_len = freq

    while (right-left+1) - freq > k:
        if nums[left] == 1:
            freq -= 1
        left += 1
    
    answer = max(answer,right-left+1)

print(answer)