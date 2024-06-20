class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        orig = x
        reversed_num = 0

        while x > 0:
            i =1
            last_digit = x % 10
            print(f"Pass {i}: last_digit {last_digit}")
            # Build the reversed number
            reversed_num = reversed_num * 10 + last_digit
            print(f"Pass {i}: reversed_num {reversed_num}")
            # Remove the last digit from x
            x = x // 10
            print(f"Pass {i}: x {x}")
            print("--------------------------------------")
        # Check if the original number is equal to the reversed number
        return orig == reversed_num

    def isstringPalindrome(self, x):
        flag = False
        if str(x) == str(x)[::-1]:
            flag = True
        return flag
# Example usage:
solution = Solution()
print(solution.isPalindrome(242))  # Output: True
print(solution.isPalindrome(-121))  # Output: False
print(solution.isPalindrome(10))   # Output: False

print("----------------------------")
print(solution.isstringPalindrome(242))  # Output: True
print(solution.isstringPalindrome(-121))  # Output: False
print(solution.isstringPalindrome(10))
