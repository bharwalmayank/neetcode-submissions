class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Anagrams contain the exact same strings with exact same frquency (not given in question)
        
        if (len (s) != len (t)): 
            return False

        # use a hashmap or a set here, treating the strings as list
        hashmapS={}
        for char in s: # in worst case runs n times
            if char not in hashmapS:
                hashmapS[char] = 1 # the value becomes relevant since we need to count frequency
            else:
                hashmapS[char] += 1
        
        hashmapT = {}
        for c in t: # in worst case run m times 
            if c not in hashmapS:
                return False
            elif c not in hashmapT:
                hashmapT[c] = 1
            else:
                hashmapT[c] += 1

        for key in hashmapS:
            if key not in hashmapT or hashmapT[key] != hashmapS[key]:
                return False

        return True