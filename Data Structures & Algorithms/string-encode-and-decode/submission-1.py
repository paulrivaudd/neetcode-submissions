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

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length
            word = s[word_start:word_end]
            res.append(word)
            i = word_end

        return res