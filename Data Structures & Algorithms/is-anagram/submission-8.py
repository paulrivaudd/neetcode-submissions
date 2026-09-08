class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        if n!=len(t):
            return False
        else:
            for car in t:
                if car in s:
                    s=s.replace(car,"",1)
                else:
                    return False
            return True 