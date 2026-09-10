class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        best=0
        for n in num_set:
            if n-1 in num_set:
                continue
            else: 
                i=0
                count=0
                while n+i in num_set:
                    count+=1
                    i+=1
            best=max(best,count)
        return best
        


