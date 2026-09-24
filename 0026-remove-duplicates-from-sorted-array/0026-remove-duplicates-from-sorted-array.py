class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = i + 1
        count = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                count += 1
            else:
                j += 1

        return count