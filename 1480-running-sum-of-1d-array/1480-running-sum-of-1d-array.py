class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        sum = 0
        for i in range(0, len(nums)):
            sum += nums[i]
            ans.append(sum)
        return ans