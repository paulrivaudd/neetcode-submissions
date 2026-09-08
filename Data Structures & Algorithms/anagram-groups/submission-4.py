class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for mot in strs:
            cle="".join(sorted(mot))
            grps.setdefault(cle, []).append(mot)
        return list(grps.values())
        


