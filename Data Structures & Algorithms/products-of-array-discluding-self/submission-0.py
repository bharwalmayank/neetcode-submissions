class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # step 1: calculate product of all numbers
        # step 2: then iterate through nums, dividing prod by it and multiply it's sign to it
        # in case, it's a 0 we resolve back to manually calculation

        prod = 1
        for n in nums:
            prod *= n
        
        res = []
        for n in range(len(nums)):
            
            if nums[n] == 0:
                lprod = 1
                for i in range(len(nums)):
                    lprod *= nums[i] if i != n else 1
                res.append(lprod)
            else:
                res.append(prod//nums[n])
            
        return res