from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=Counter(nums)
        resnew=res.most_common(k)
        final=[]
        for (num,nb) in resnew:
            final.append(num)
        return final 

