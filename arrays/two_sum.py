# Two Sum Problem
# Hints
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Brutforce method
def twoSum(self, nums, target):
    """
    nums: list
	target: int
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Optimized method using hash map
def twoSum_optimized(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        # Calculate the complement we need to find
        complement = target - num
        # If complement exists in our map, we found our answer
        if complement in num_map:
            return [num_map[complement], i]
        # Store the current number and its index
        num_map[num] = i
    
    # No solution found (though problem states there will always be one)
    return []