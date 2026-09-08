class Solution:
    from collections import Counter
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for mot in strs:
            cle="".join(sorted(mot))
            if cle in grps:
                grps[cle].append(mot)
            else:
                grps[cle]=[mot]
        return list(grps.values())
        


