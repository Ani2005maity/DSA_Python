class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        ans = []
        ind = 0
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                ans.insert(ind, nums[i])
                ind += 1
            else:
                ans.append(nums[i])

        return ans