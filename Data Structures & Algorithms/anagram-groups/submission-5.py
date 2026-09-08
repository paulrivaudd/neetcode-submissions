class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = {}
        for mot in strs:
            compte = [0] * 26
            for car in mot:
                compte[ord(car) - ord("a")] += 1
            cle = tuple(compte)                        # apres la boucle interne
            grps.setdefault(cle, []).append(mot)
        return list(grps.values())
        

