class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # comparing set lenght to the list length is not a good solution
        # brute force is just going over every combination twice using
        # two for loops, use a hashmap with keys as the nums and values as the frequency

        hashmap = {} # also called a dictionary in python
        for item in nums:
            if item in hashmap:
                return True
            else:
                hashmap[item] = 1
        return False