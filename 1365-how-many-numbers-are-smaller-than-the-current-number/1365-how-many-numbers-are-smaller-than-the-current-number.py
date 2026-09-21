class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        i = 0
        ans = []
        while i < len(nums):
            count = 0
            for j in range(0, len(nums)):
                if nums[j] < nums[i]:
                    count += 1
                
            ans.append(count)
            i += 1
            
        return ans