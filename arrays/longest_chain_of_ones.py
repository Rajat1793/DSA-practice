# Longest Chain of Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array. The task is to determine the longest sequence of ones in the binary list, where ones represent consecutive occurrences of a certain condition.

# For example, consider the following cases:

# Example 1:
# Input: nums = [1, 0, 1, 1, 0, 1]
# Output: 2
# Explanation: The first two occurrences of 1 and two 1s together form sequences. The maximum is two consecutive 1's.

# Example 2:
# Input: nums = [1, 1, 0, 1, 1, 1]
# Output: 3
# Explanation: The last three 1's are consecutive, forming the longest sequence of 1's.

# Your goal is to identify such sequences of 1's in the input array and return the length of the longest sequence, ensuring that your solution is efficient enough to handle large inputs.

# How to Solve "Longest Chain of Ones" Problems: 10-Point Guide

# 1. **Recognize the pattern**: This is a "consecutive elements" counting problem, which typically requires tracking sequences as you iterate through an array.
# 2. **Use two counter variables**: One to track the current consecutive count and another to track the maximum count seen so far.
# 3. **Start with zero values**: Initialize both current_count and max_count to 0 before you begin iterating.
# 4. **Process one element at a time**: Iterate through the array once from beginning to end in a single pass.
# 5. **Apply the counting logic**: If the current element is what you're counting (1 in this case), increment your current counter; otherwise, reset it to 0.
# 6. **Update the maximum after each element**: Use max(max_count, current_count) to keep track of the longest sequence found.
# 7. **Handle edge cases**: Consider what happens at the beginning and end of the array, though this particular problem doesn't have special edge cases.
# 8. **Focus on the linear solution**: Avoid nested loops - this problem can always be solved in O(n) time with O(1) space.
# 9. **Visualize the counter changes**: As you trace through an example, track how current_count rises and falls while max_count only increases.
# 10. **Remember the reset condition**: The key insight is knowing when to reset your counter (when you encounter a 0 in this problem).
# This approach will work for similar "longest consecutive sequence" problems with minor adaptations to the specific requirements.

# BruteForce method
def findMaxConsecutiveOnes_brute_force(nums):
    # Step 1: Initialize variables to track results
    max_consecutive = 0
    
    # Step 2: Iterate through all possible subarrays
    for i in range(len(nums)):
        # Step 3: Count consecutive ones starting at position i
        count = 0
        for j in range(i, len(nums)):
            # If we find a zero, break the chain
            if nums[j] == 0:
                break
            # Otherwise, increment the count
            else:
                count += 1
        
        # Step 4: Update the maximum if current count is larger
        max_consecutive = max(max_consecutive, count)
    
    # Step 5: Return the result
    return max_consecutive

# Optimized code
def findMaxConsecutiveOnes_optimized(nums):
    # Step 1: Initialize variables to track current and maximum count
    current_count = 0
    max_count = 0
    
    # Step 2: Iterate through the array once
    for num in nums:
        # Step 3: If current element is 1, increment counter
        if num == 1:
            current_count += 1
        # Step 4: If current element is 0, reset counter
        else:
            current_count = 0
        
        # Step 5: Update maximum count if current count is larger
        max_count = max(max_count, current_count)
    
    # Step 6: Return the maximum count
    return max_count