# Discover Duplicates in a Bag

# Given an integer array nums of length n where all integers are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appear twice.
# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output.

# Example 1:
# Input: nums = [5,4,3,7,6,3,4,8]
# Output: [3,4]

# Example 2:
# Input: nums = [2,2,3]
# Output: [2]

# Example 3:
# Input: nums = [2]
# Output: []

# In this problem, you are expected to find all numbers that occur twice in the given array, adhering to the specified time and space complexity constraints.

# Constraints
# The length of nums (n) is in the range [1, 10^5]
# Each integer in nums is in the range [1, n]
# Each integer appears at most twice.

## Step-by-Step Problem-Solving Guide:
# 1. **Understand the constraint**: All integers are in range [1,n], which means they can be mapped to array indices.
# 2. **Identify the key insight**: We can use the array itself as our "hash table" by marking elements.
# 3. **Choose the marking method**: Flipping the sign (making elements negative) at the index corresponding to the number.
# 4. **Process each element**: For each number, check the element at the index corresponding to that number.
# 5. **Detect duplicates**: If the element at that index is already negative, we've seen this number before.
# 6. **Handle the indexing**: Since arrays are 0-indexed but our numbers start at 1, subtract 1 from each number.
# 7. **Use absolute value**: When checking indices, use the absolute value of numbers (since we're making them negative).
# 8. **Build the result**: Add each duplicate to our result array.
# 9. **No extra space**: The solution modifies the input array in-place for marking.
# 10. **Validate correctness**: Test with the examples to ensure the solution works.

# BruteForce Method
def findDuplicates_brute_force(nums):
    # Step 1: Initialize result array
    result = []
    
    # Step 2: Check each number against all others
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Step 3: If duplicate found and not already in result, add it
            if nums[i] == nums[j] and nums[i] not in result:
                result.append(nums[i])
    result.sort()
    return result

# Optimized Method
def findDuplicates_optimized(nums):
    # Step 1: Initialize result array
    result = []
    
    # Step 2: Iterate through the array
    for num in nums:
        # Get the absolute value (in case it's been marked negative)
        index = abs(num) - 1
        
        # Step 3: Check if we've seen this number before
        if nums[index] < 0:
            # We've seen this number before, add to result
            result.append(abs(num))
        else:
            # Mark this number as seen by making the element at its index negative
            nums[index] = -nums[index]
    result.sort()
    return result