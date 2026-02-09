import collections
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        firstIndex = scIndex = None
        for index in range(len(s1)):
            if s1[index] == s2[index]:
                continue
            count += 1
            scIndex = firstIndex 
            firstIndex = index
            if count > 2:
                return False
        if count == 0:
            return True
        elif count == 1:
            return False
        elif s1[scIndex] == s2[firstIndex] and s1[firstIndex] == s2[scIndex]:
            return True
        else:
            return False
