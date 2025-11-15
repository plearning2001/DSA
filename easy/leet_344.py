from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        fst_point = 0
        snd_point = len(s)-1

        while fst_point<snd_point:
            s[fst_point],s[snd_point] = s[snd_point],s[fst_point]

            fst_point +=1
            snd_point -=1
        
        return s




answer_object = Solution()
data1 = ["h","e","l","l","o"]
data = ["H","a","n","n","a","h"]
answer = answer_object.reverseString(data)
print(f"answer - {answer}")
