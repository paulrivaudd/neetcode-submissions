class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        get=freq.get
        for x in nums:
            freq[x]=get(x,0)+1
        
        buckets=[[]for _ in range(len(nums)+1)]
        for val,cnt in freq.items():
            buckets[cnt].append(val)

        res=[]
        for cnt in range(len(nums),0,-1):
            for val in buckets[cnt]:
                res.append(val)
                if len(res)==k:
                    return res
        return res 