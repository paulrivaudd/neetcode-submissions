class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Passe 1 : output[i] = produit de nums[0..i-1]
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]

        # Passe 2 : on multiplie par le produit de droite, accumulé dans une variable
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output