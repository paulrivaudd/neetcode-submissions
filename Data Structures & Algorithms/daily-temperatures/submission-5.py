class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0] * len(temperatures)
        pile=[]
        for i in range(len(temperatures)):
            while pile and temperatures[pile[-1]]<temperatures[i]:
                j=pile.pop()
                result[j]=i-j
            pile.append(i)
        return result 