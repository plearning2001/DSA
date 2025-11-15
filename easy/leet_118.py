from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        parent_row = []
        first_row = [1]
        parent_row.append(first_row)
        for i in range(1,numRows):
            print(i)
            new_row = [1]
            for j in range(1,i):
                new_row.append(previous_row[j]+previous_row[j-1])
                print("hi")
            new_row.append(1)
            parent_row.append(new_row)
            previous_row = new_row
        
        return parent_row



answer_object = Solution()
num = 2
answer = answer_object.generate(num)
print(f"answer - {answer}")
