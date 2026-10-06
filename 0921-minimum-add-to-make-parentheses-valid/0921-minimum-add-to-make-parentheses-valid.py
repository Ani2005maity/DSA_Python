class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        ans = 0
        for val in s:
            if val == '(':
                count += 1
            elif val == ')':
                count -= 1
            if count < 0:
                ans += 1
                count = 0
            else:
                continue
        return ans + count