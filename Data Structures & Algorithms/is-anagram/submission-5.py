class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26
        base = ord('a')
        for ch in s:
            counts[ord(ch) - base] += 1
        for ch in t:
            counts[ord(ch) - base] -= 1
            if counts[ord(ch) - base] < 0:
                return False
        return True