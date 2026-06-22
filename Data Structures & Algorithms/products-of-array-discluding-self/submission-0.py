import math 
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        n=len(nums)
        for i in range(n):
            nums_i = nums[:i] + nums[i+1:]
            output.append(math.prod(nums_i))
        
        return output

    
            
    