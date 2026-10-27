class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # naive O (n^2) solution, use nested for loops
        # Hashmap solution, put everything in a hashmap

        hash = set()
        for i in nums:
            if i in hash:
                return True
            else:
                hash.add(i)
        return False