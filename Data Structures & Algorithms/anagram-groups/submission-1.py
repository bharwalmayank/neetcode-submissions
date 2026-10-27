class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # how do you encode equality in this case?
        # equal frequency, order irrelevant
        # use a hash dataset to store the frequency map as immutable key
        # then use that key in the dictionary to group, group by design not simulation

        groupings = defaultdict(list) # default dictionary assigns empty list to missing keys
        
        for word in strs:
            counts = [0] * 26
            for alph in word:
                counts[ord(alph) - ord('a')] += 1
            groupings[tuple(counts)].append(word)

        return list(groupings.values())