from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=Counter(nums)
        resnew=res.most_common(k)
        result=[]
        for (num,nb) in resnew:
            result.append(num)
        return result 
