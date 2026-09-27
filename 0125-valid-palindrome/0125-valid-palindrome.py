class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for val in s:
            if val.isalnum():
                temp += val.lower()

        return temp == temp[::-1]