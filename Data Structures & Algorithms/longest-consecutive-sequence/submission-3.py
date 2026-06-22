class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        count = 1
        best = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue

            if nums[i] + 1 == nums[i + 1]:
                count += 1
            else:
                best = max(best, count)
                count = 1

        return max(best, count)