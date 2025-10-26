# Maximum Subarray
# Leetcode -> 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The array contains only one element, which is the max subarray.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The entire array is the largest subarray with sum = 23.

# Note
# A subarray is a contiguous part of an array. In the above problem, you're required to find the subarray which has the maximum sum.
# It's possible for the input array to have negative numbers, and the optimal subarray might start or end at a negative number to maximize the overall sum.

# Constraints
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

## Step-by-Step Problem-Solving Guide:
# 1. **Understand the problem**: We need to find a contiguous subarray with the largest sum.
# 2. **Identify the key insight**: At each position, we have two choices:
#   - Start a new subarray from the current element
#   - Extend the previous subarray by including the current element
# 3. **Apply Kadane's Algorithm**:
#   - Keep track of the maximum subarray sum ending at each position
#   - Choose the better option: start fresh or extend previous subarray
#   - Track the overall maximum sum found so far
# 4. **Initialize properly**: Start with the first element for both current and maximum sums.
# 5. **Process each element**: For each number, decide if it's better to start a new subarray or continue the existing one.
# 6. **Update the maximum**: Keep track of the highest sum found during the process.
# 7. **Handle edge cases**: The algorithm works even with arrays containing a single element.
# 8. **Consider all-negative arrays**: The solution will correctly return the largest (least negative) element.

# BruteForce Method
def maxSubArray_brute_force(nums):
    # Step 1: Initialize maximum sum to the smallest possible value
    max_sum = float('-inf')
    
    # Step 2: Try all possible subarrays
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            # Step 3: Add current element to the sum
            current_sum += nums[j]
            
            # Step 4: Update maximum if current sum is larger
            max_sum = max(max_sum, current_sum)
    
    return max_sum

# Optimized Approach ( Kadane's Algorithm )
def maxSubArray_optimized(nums):
    # Step 1: Initialize variables
    max_sum = nums[0]  # Maximum sum found so far
    current_sum = nums[0]  # Sum of the current subarray
    
    # Step 2: Iterate through the array starting from second element
    for i in range(1, len(nums)):
        # Step 3: Decide whether to extend previous subarray or start a new one
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Step 4: Update the maximum sum if current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum