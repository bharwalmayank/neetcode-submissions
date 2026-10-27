class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS = {}
        dictT = {}

        for i in s:
            if i not in dictS:
                dictS[i] = 1
            else:
                dictS[i] += 1

        for g in t:
            if g not in dictT:
                dictT[g] = 1
            else:
                dictT[g] += 1
        return dictT == dictS