# 448. Find All Numbers Disappeared in an Array

# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n

## Step-by-Step Problem-Solving Guide:
# 1. **Identify the key constraint**: The numbers in the array are between 1 and n.
# 2. **Use this constraint to our advantage**: We can use the indices of the array as a hash table.
# 3. **Mark seen numbers**: For each number, mark the corresponding index (number-1) as seen.
# 4. **Choose a marking method**: Make the value at that index negative without losing the original value.
# 5. **Process the array**: Go through each number and mark its corresponding index.
# 6. **Find unmarked indices**: After marking, any index that's still positive corresponds to a missing number.
# 7. **Map back to the original values**: Add 1 to each unmarked index to get the missing number.
# 8. **Handle duplicates**: Use absolute value when accessing indices to account for already-marked numbers.
# 9. **Preserve information**: We need the original values for marking, so we use sign flipping instead of replacement.
# 10. **Collect results**: Gather all missing numbers in the output array.

# BruteForce Method
def findDisappearedNumbers_brute_force(nums):
    # Step 1: Get the length of the array
    n = len(nums)
    
    # Step 2: Create a result array to hold missing numbers
    result = []
    
    # Step 3: Check each number from 1 to n
    for i in range(1, n + 1):
        # Step 4: If the number is not in the array, add it to result
        if i not in nums:
            result.append(i)
    
    return result


# Optimized method using Array Marking
def findDisappearedNumbers(nums):
    # Convert array to set for O(1) lookups
    num_set = set(nums)
    
    # Find numbers from 1 to n that aren't in the set
    result = []
    for i in range(1, len(nums) + 1):
        if i not in num_set:
            result.append(i)
            
    return result