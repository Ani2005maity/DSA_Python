class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        ans = 0

        for val in s:
            if val == '(':
                count += 1
                ans = max(ans, count)

            elif val == ')':
                count -= 1

        return ans