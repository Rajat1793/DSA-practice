# Find the Missing Number in an Array

# Given an array nums containing n distinct numbers in the range ([0, n]), 
# return the only number in the range that is missing from the array.

# Example:
# Input: nums = [3, 0, 1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range 0-3. 2 is the number missing from the array.

# Input: nums = [0, 1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range 0-2. 2 is the missing number.

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range 0-9. 8 is the missing number.

# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range 0-1. 1 is the missing number.

# Constraints
# 1 <= nums.length <= 100
# 0 <= nums[i] <= n (where n is the length of the array)
# nums contains distinct numbers only.

## Step-by-Step Problem-Solving Guide:
# 1. **Understand the problem**: We have n distinct numbers in the range 0 to n, with one number missing.
# 2. **Consider what we know**: The array has n elements, so the complete range would be 0 to n.
# 3. **Think of mathematical properties**: The sum of numbers from 0 to n is n*(n+1)/2.
# 4. **Identify the key insight**: The difference between the expected sum and the actual sum must be the missing number.
# 5. **Apply the formula**: Calculate the expected sum of all numbers from 0 to n.
# 6. **Calculate the actual sum**: Sum all elements in the given array.
# 7. **Find the difference**: Subtract the actual sum from the expected sum.
# 8. **Return the result**: The difference is our missing number.
# 9. **Consider edge cases**: The solution works even if the missing number is 0 or n.
# 10. **Verify the solution**: Test with the provided examples to ensure correctness.

# BruteForce Method
def missingNumber_brute_force(nums):
    # Step 1: Determine the range we should check
    n = len(nums)
    
    # Step 2: Check each number from 0 to n
    for i in range(n + 1):
        # Step 3: If the current number is not in the array, return it
        if i not in nums:
            return i
    
    # This should never happen with the problem constraints
    return -1

# Optimized Solution
def missingNumber_optimized(nums):
    # Step 1: Calculate the expected sum of numbers from 0 to n
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    
    # Step 2: Calculate the actual sum of the array
    actual_sum = sum(nums)
    
    # Step 3: The difference is the missing number
    return expected_sum - actual_sum