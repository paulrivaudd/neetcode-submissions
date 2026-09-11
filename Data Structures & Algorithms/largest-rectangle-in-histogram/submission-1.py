class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pile=[]
        aire=0
        for i in range(len(heights)):
            while pile and heights[pile[-1]]>heights[i]:
                j=pile.pop()
                largeur = i - pile[-1] - 1 if pile else i
                aire_rect = largeur * heights[j]
                aire = max(aire, aire_rect)
            pile.append(i)
        n = len(heights)
        while pile:
            j = pile.pop()
            largeur = n - pile[-1] - 1 if pile else n
            aire = max(aire, largeur * heights[j])    
        return aire  