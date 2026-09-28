class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        count = 0
        size = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                continue
            else:
                if count == 0:
                    size = len(s[i])
                    count += 1
            return size