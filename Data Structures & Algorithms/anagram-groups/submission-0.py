
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        res = {}
        for i in range(n):
            key = "".join(sorted(strs[i]))  #on trie les caractères en une liste puis on les réunit de nv avec join
            if key not in res:
                res[key] = [strs[i]]
            else:
                res[key].append(strs[i])
        return list(res.values())