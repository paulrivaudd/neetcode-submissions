class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=Counter(nums)  #create a dict {value:occurence}
        resnew= res.most_common(k) #returns most frequent couple 
        result=[]
        for (num,nb) in resnew:
            result.append(num)
        return result 