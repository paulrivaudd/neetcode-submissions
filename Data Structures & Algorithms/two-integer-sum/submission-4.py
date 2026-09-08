class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vu = {}                                # valeur -> indice
        for i, n in enumerate(nums):
            complement = target - n
            if complement in vu:
                return [vu[complement], i]
            vu[n] = i
        return []