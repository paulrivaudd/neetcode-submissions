class Solution:
    def isValid(self, s: str) -> bool:
        dict={')':'(', '}':'{', ']':'['}
        pile=[]

        for c in s:
            if c in dict:
                if not pile or pile[-1]!=dict[c]:
                    return False
                pile.pop()
            else:
                pile.append(c)
        return not pile