class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # step 1: calculate product of all numbers
        # step 2: then iterate through nums, dividing prod by it and multiply it's sign to it
        # in case, it's a 0 we resolve back to manually calculation

        prod = 1
        prod_nz = 1
        n_z = 0
        for n in nums:
            prod *= n
            if n!=0:
                prod_nz *= n
            n_z += 1 if n==0 else 0
        
        res = []
        for n in range(len(nums)):
            
            if nums[n] == 0 and n_z <= 1:
                res.append(prod_nz)
            elif n_z > 1:
                res.append(0)
            else:
                res.append(prod//nums[n])
            
        return res