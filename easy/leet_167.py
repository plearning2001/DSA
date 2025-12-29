nums = [2,3,4]
target = 6

i = 0
j = len(nums)-1

while i < j:
   if nums[i]+nums[j] == target:
      print([i+1,j+1])
      break
   elif nums[i]+nums[j] > target:
      j -=1
   elif nums[i]+nums[j] < target:
      i +=1

      