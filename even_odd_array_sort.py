# Even Odd Array Sort

# You are given an array nums consisting of integers where half of the numbers are even, and the other half are odd. Your objective is to rearrange the array such that each even number appears at an even index, and each odd number appears at an odd index.

# Return any array that meets these sorting requirements.

# Example 1:
# Input: nums = [3,2,4,7]
# Output: [2,3,4,7]

# Example 2:
# Input: nums = [2,3]
# Output: [2,3]
# In this example, the number 2 (even) is positioned at an even index (0), and the number 3 (odd) is positioned at an odd index (1). Any permutation that satisfies these conditions is acceptable.

# Constraints
# len(nums) % 2 == 0
# 0 <= nums[i] <= 10^4

## Step-by-Step Problem-Solving Guide:
# 1. **Understand the problem**: We need to position even numbers at even indices and odd numbers at odd indices.
# 2. **Identify the key insight**: The number of even and odd elements must be equal (given in the problem).
# 3. **Consider the approach**: We need to identify even/odd numbers and place them at the correct positions.
# 4. **Plan the algorithm**: Either separate first, then place, or use two pointers to place directly.
# 5. **Handle the placement**: Even numbers go to indices 0, 2, 4..., and odd numbers go to indices 1, 3, 5...
# 6. **Implement the solution**: Either with separation or with two pointers tracking available positions.
# 7. **Check edge cases**: The problem guarantees that there are equal numbers of even and odd elements, so no special handling needed.
# 8. **Verify the solution**: Ensure all even numbers are at even indices and all odd numbers are at odd indices.
# 9. **Optimize if needed**: The two-pointer solution is already optimal at O(n) time.
# 10. **Test with examples**: Verify the solution with the provided examples.

# BruteForce Method
def sortArrayByParityII_brute_force(nums):
    # Step 1: Separate even and odd numbers
    even_numbers = [num for num in nums if num % 2 == 0]
    odd_numbers = [num for num in nums if num % 2 == 1]
    
    # Step 2: Create a new result array
    result = [0] * len(nums)
    
    # Step 3: Place even numbers at even indices
    for i in range(0, len(nums), 2):
        result[i] = even_numbers[i//2]
    
    # Step 4: Place odd numbers at odd indices
    for i in range(1, len(nums), 2):
        result[i] = odd_numbers[i//2]
    
    return result

# Optimized method
def sortArrayByParityII_optimized(nums):
    # Step 1: Initialize two pointers
    even_index = 0  # Points to even indices (0, 2, 4...)
    odd_index = 1   # Points to odd indices (1, 3, 5...)
    n = len(nums)
    result = [0] * n
    
    # Step 2: Iterate through the original array
    for num in nums:
        # Step 3: If number is even, place at even index
        if num % 2 == 0:
            result[even_index] = num
            even_index += 2
        # Step 4: If number is odd, place at odd index
        else:
            result[odd_index] = num
            odd_index += 2
    
    return result