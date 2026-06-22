from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # On cherche le caractère # qui sépare la longueur du mot
            while s[j] != "#":
                j += 1

            # La longueur du mot est entre i et j
            length = int(s[i:j])

            # Le mot commence juste après le #
            word_start = j + 1
            word_end = word_start + length

            # On récupère exactement length caractères
            word = s[word_start:word_end]
            res.append(word)

            # On avance au prochain bloc
            i = word_end

        return res