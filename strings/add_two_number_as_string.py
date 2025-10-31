# Add Two Large Numbers as Strings
# Leetcode -> 415. Add Strings

# Problem Description:
# Given two non-negative integers, num1 and num2 represented as strings, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers. Also, you must not directly convert the inputs to integers.

# Example 1:
# Input: num1 = "23", num2 = "74"
# Output: "97"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

# Constraints:
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 do not have any leading zeros except for the zero itself.

# Custom Instructions:
# This is an EASY problem.
# To solve this problem, treat the string representations of the numbers as sequences of characters. Start adding from the rightmost character to the leftmost, while taking care of the carry that results from adding two digits that sum to more than 9. The objective is to perform the addition as you would manually on paper. Avoid using direct conversions of the whole string to integer values.

## Step-by-Step Problem-Solving Guide:
# 1. **Understand the problem**: We need to add two numbers represented as strings without converting them to integers directly.
# 2. **Simulate manual addition**: Start from the rightmost digit and work towards the left, just like manual addition.
# 3. **Handle digits one by one**: Convert each character to its numeric value and add them together.
# 4. **Track the carry**: When adding two digits, remember to include any carry from the previous addition.
# 5. **Build the result**: Construct the result string digit by digit.
# 6. **Handle different length strings**: Make sure to process both strings completely, even if one is longer than the other.
# 7. **Add final carry**: Don't forget any remaining carry after processing all digits.
# 8. **Return the result**: Join all digits into a single string.


# Brute Force Method
def addStrings_brute_force(num1, num2):
    # Step 1: Initialize variables
    result = []
    carry = 0
    
    # Step 2: Pad the shorter string with leading zeros
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)
    
    # Step 3: Iterate from right to left
    for i in range(max_length - 1, -1, -1):
        # Step 4: Get current digits and calculate sum
        digit1 = int(num1[i])
        digit2 = int(num2[i])
        digit_sum = digit1 + digit2 + carry
        
        # Step 5: Update carry and add current digit to result
        carry = digit_sum // 10
        current_digit = digit_sum % 10
        result.insert(0, str(current_digit))
    
    # Step 6: Add final carry if needed
    if carry > 0:
        result.insert(0, str(carry))
    
    # Step 7: Join and return the result
    return ''.join(result)

# Optimized Method
def addStrings_optimized(num1, num2):
    # Step 1: Initialize result and pointers
    result = []
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    
    # Step 2: Process both strings from right to left
    while i >= 0 or j >= 0 or carry:
        # Step 3: Get digits at current positions (0 if exhausted)
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        
        # Step 4: Calculate sum and new carry
        digit_sum = digit1 + digit2 + carry
        carry = digit_sum // 10
        
        # Step 5: Add current digit to result
        result.append(str(digit_sum % 10))
        
        # Step 6: Move pointers
        i -= 1
        j -= 1
    
    # Step 7: Reverse and join the result
    return ''.join(result[::-1])