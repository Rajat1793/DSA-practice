# Check for Duplicates in an Array
# 287. Find the Duplicate Number

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

## Step-by-Step Problem-Solving Guide:
# 1. **Recognize the pattern**: This is a "find duplicates" problem, perfect for using a hash set.
# 2. **Use a set for O(1) lookups**: Sets give constant-time membership testing.
# 3. **Process elements one by one**: Check each element against previously seen ones.
# 4. **Return early when possible**: As soon as we find a duplicate, we can return True.
# 5. **Maintain the set**: Add each new element to our set of seen values.
# 6. **Only return False at the end**: We must process all elements to determine no duplicates exist.
# 7. **Consider alternatives**: Sorting is another approach (O(n log n)), but hash set is more efficient.
# 8. **Handle constraints**: The problem has a large array size (up to 10^5), making O(n²) solutions too slow.
# 9. **Consider space usage**: The hash set solution uses O(n) space, which is acceptable for this problem.
# 10. **Test with examples**: Verify the solution with the provided examples.

# BruteForce Method
def containsDuplicate_brute_force(nums):
    # Step 1: Check each element against all other elements
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            # Step 2: If duplicate found, return True
            if nums[i] == nums[j]:
                return True
    
    # Step 3: No duplicates found
    return False

# Optimized method using HASHSET
def containsDuplicate_optimized(nums):
    # Step 1: Create a set to track seen elements
    seen = set()
    # Step 2: Iterate through the array
    for num in nums:
        # Step 3: Check if the current number has been seen before
        if num in seen:
            return True
        # Step 4: Add current number to the set
        seen.add(num)
    
    # Step 5: No duplicates found
    return False

# Optimized using sorting
def containsDuplicate_sorting(nums):
    # Step 1: Sort the array
    nums.sort()
    
    # Step 2: Check adjacent elements for duplicates
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    
    # Step 3: No duplicates found
    return False