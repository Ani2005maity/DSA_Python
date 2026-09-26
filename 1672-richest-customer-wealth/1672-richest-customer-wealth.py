class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans = 0
        for row in accounts:
            temp = 0

            for value in row:
                temp += value

            ans = max(ans, temp)

        return ans