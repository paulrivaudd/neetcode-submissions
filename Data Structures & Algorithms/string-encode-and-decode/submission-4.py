class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [],  0
        while i<len(s):
            j=i
            while s[j]!="#": #on passe tant qu'on a pas un # qui marque la séparation entre la longueur et le mot 
                j+=1
            lenght=int(s[i:j])  # de i à j exclu, convertit la chaîne en entier pour avvoir la longueur
            res.append(s[j + 1 : lenght + j + 1 ]) # on ajoute la chaîne de caractère après le #
            i= j+ 1 + lenght # on actualise la longueur 
        return res


