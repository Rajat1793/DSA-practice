# Minimum Apples Addition to Organize Bags

# John is a passionate fruit collector and has an interesting hobby of organizing his fruits in a line. He has a collection of fruit bags containing a certain number of fruits, which can be represented as an integer array nums (0-indexed). 
# Every day, he ensures that each of his fruit bags contains more fruits than the one before it, thereby creating a strictly increasing order of fruit count.
# However, he can only add more fruits to any bag; removing them is not an option. In a single operation, Hitesh can choose any bag and increment its fruit count by 1.
# The task at hand is to determine the minimum number of operations required to make this arrangement strictly increasing. 
# An array nums is strictly increasing if for all 0 <= i < nums.length - 1, nums[i] < nums[i+1]. If the array contains only one bag, it is trivially in a strictly increasing order.

# Example 1:
# Input: nums = [2,2,2]
# Output: 3
# Explanation: You can do the following operations:
# 1) Increment nums[1], so nums becomes [2,3,2].
# 2) Increment nums[2], so nums becomes [2,3,3].
# 3) Increment nums[2], so nums becomes [2,3,4].

# Example 2:
# Input: nums = [3,10,3,8,2]
# Output: 15

# Example 3:
# Input: nums = [10]
# Output: 0

# Constraints
# 1 <= nums.length <= 5000
# 1 <= nums[i] <= 10^4

## Step-by-Step Problem-Solving Guide:
# 1. **Handle the base case**: If there's only one element, no operations are needed.
# 2. **Maintain a running minimum**: Keep track of the minimum value the next element should have.
# 3. **Process elements sequentially**: For each element, check if it needs to be incremented.
# 4. **Calculate increments**: If an element is not greater than the previous, calculate how many increments are needed.
# 5. **Update the running total**: Add the required increments to the total operations count.
# 6. **Update previous value**: After processing an element, update the "previous value" for the next comparison.
# 7. **No need for array modification**: In the optimized solution, we don't need to modify the original array.
# 8. **Focus on minimum increments**: Always increment just enough to make the current element one more than the previous.
# 9. **Consider all elements**: Process the entire array to find the total operations needed.
# 10. **Verify with examples**: Test your solution with the provided examples to ensure correctness.

# BruteForce Method 
def minIncrementForIncreasing_brute_force(nums):
    # Step 1: If there's only one element, no operations needed
    if len(nums) <= 1:
        return 0
    
    # Step 2: Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Step 3: If current element is not greater than previous
        if nums[i] <= nums[i-1]:
            # Step 4: Calculate increments needed
            increment= nums[i-1] - nums[i] + 1
            # Step 5: Update the current element
            nums[i] += increment
            # Step 6: Add to total operations
            operations += increment
    return operations
