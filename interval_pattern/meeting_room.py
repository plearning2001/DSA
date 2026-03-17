'''
## 🔥 Problem 3: Meeting Rooms I

### Real Life Story
You got **invited to many meetings** today.
Can **ONE person** attend ALL of them without any clash?
```
Meetings: [9,10], [9,12], [11,13]
```
**Answer: NO** → `[9,10]` and `[9,12]` clash at 9!

'''

def can_attend_all(meetings):
    # Sort by start time
    meetings.sort(key=lambda x: x[0])
    
    for i in range(1, len(meetings)):
        prev = meetings[i-1]
        curr = meetings[i]

        if curr[0] < prev[1]:
            return False   # can't attend all ❌

    return True  

print(can_attend_all([[9,10],[9,12],[11,13]]))
print(can_attend_all([[1,3],[4,6],[7,9]]))
print(can_attend_all([[1,5],[4,8]]))