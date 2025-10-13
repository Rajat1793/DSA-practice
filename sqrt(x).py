# Find a Sqrt(x) without using the inbuilt function

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should also be non-negative.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in C++ or x ** 0.5 in Python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# Constraints:
# 0 <= x <= 2^{31} - 1

# Constraints
# 0 <= x <= 2^{31} - 1

# Bruteforce method
def mySqrt_brute_force(x):
    if x == 0:
        return 0
    i = 1
    while i * i <= x:
        i += 1
    return i - 1

# Optimized method binary search
def mySqrt_optimized(x):
    if x == 0:
        return 0
    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    return left

print(mySqrt_brute_force(8))
print(mySqrt_optimized(8))