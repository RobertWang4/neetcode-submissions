from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        count1 = Counter(s1)
        count2 = Counter(s2[:k])

        if count1 == count2:
            return True

        for i in range(k,len(s2)):
            count2[s2[i]] += 1
            count2[s2[i-k]] -= 1

            if count2[s2[i-k]] == 0:
                del count2[s2[i-k]]
            
            if count1 == count2:
                return True
        
        return False
            