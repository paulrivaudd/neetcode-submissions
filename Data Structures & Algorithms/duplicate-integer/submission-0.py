class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range (n):
            for j in range (n):
                if nums[i]==nums[j] and i!=j:
                    return True
        return False 

