class Solution:
    def countDigits(self, num: int) -> int:
        n = num
        count = 0
        while n > 0:
            el = n % 10
            if num % el == 0:
                count += 1
            n //= 10

        return count