class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            n_target=target-nums[i]
            for j in range(n):
                if i!=j and n_target-nums[j]==0:
                    return [i,j]
        return False