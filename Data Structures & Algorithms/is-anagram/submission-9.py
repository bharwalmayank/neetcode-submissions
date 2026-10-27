class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        # use a hashmap to map alphabets with frequencies for both s and t
        # if both hashmaps don't match return false, else return true

        hashmap1 = {}
        hashmap2 = {}

        for i in s:
            if i not in hashmap1:
                hashmap1[i] = 1
            else:
                hashmap1[i] += 1

        for j in t:
            if j not in hashmap2:
                hashmap2[j] = 1
            else:
                hashmap2[j] += 1

        return hashmap1 == hashmap2