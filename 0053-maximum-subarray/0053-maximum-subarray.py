class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        asum = nums[0]
        tsum = 0  
        for i in range(0, len(nums)):
            tsum += nums[i]
            asum = max(tsum, asum)
            if(tsum < 0):
                tsum = 0

        return asum