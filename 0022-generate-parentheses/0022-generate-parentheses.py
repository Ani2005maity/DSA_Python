class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def backtract(s, open, close):
            if len(s) == 2 * n:
                ans.append(s)
                return
            
            if open < n:
                backtract(s + "(", open + 1, close)

            if close < open:
                backtract(s + ")", open, close + 1)

        backtract("", 0, 0)
        return ans