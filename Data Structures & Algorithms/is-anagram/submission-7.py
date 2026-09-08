class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count={}
        for car in s:
            count[car]= count.get(car,0) + 1 
        for car in t:
            if count.get(car,0) == 0:
                return False
            count[car]-=1
        return True 