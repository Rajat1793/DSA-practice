# Find the Unique Number in the Array

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Examples
# Example 1:
# Input: nums = [1,2,1,3,2]
# Output: 3
# Explanation: Every number appears twice except for the number '3'.

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Explanation: Every number appears twice except for the number '4'.

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: The array contains only one number.

# Constraints
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears once.

## Step-by-Step Problem-Solving Guide:
# 1. **Understand the key properties of XOR**:
#   - XOR of a number with itself is 0: `a ^ a = 0`
#   - XOR of a number with 0 is the number itself: `a ^ 0 = a`
#   - XOR is commutative and associative: `a ^ b = b ^ a` and `(a ^ b) ^ c = a ^ (b ^ c)`
# 2. **Apply these properties to our problem**:
#   - When we XOR all numbers, the pairs will cancel out (become 0)
#   - The only remaining number will be the one without a pair
# 3. **Initialize a variable** to store the running XOR result, starting with 0
# 4. **Process each element** in the array by XORing it with our result
# 5. **The final result** is the unique number

# Bruteforce Method
def singleNumber_brute_force(nums):
    # Step 1: Check each number against all others
    for num in nums:
        # Step 2: Count occurrences of current number
        count = 0
        for n in nums:
            if n == num:
                count += 1
        
        # Step 3: If count is 1, we found the unique number
        if count == 1:
            return num
        
# Optimized using XOR
def singleNumber_optimized(nums):
    # Step 1: Initialize result to 0
    result = 0
    
    # Step 2: XOR all numbers in the array
    for num in nums:
        result ^= num
    
    # Step 3: Return the result (the unique number)
    return result