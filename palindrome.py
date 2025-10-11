# Checking for Palindrome Numbers
# Hints
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Constraints
# 2^31 <= x <= 2^31 - 1

# Brutforce method
def isPalindrome(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]
print(isPalindrome(121))

# optimized version ChatGPT
def isPalindrome_optimized(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        # Add the last digit of x to reversed_half
        reversed_half = reversed_half * 10 + x % 10
        # Remove the last digit from x
        x //= 10

    # For even length, x == reversed_half
    # For odd length, x == reversed_half // 10 (middle digit doesn't matter)
    return x == reversed_half or x == reversed_half // 10