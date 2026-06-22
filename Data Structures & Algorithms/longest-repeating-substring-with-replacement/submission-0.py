class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        count={}
        left=0
        maxFreq=0
        max_len=0
        L=0
        for right in range(n):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFreq=max(count.values())
            L=right-left+1
            if L-maxFreq>k:
                count[s[left]]-=1
                left+=1
                L-=1
            max_len=max(max_len,L)
        return max_len            
