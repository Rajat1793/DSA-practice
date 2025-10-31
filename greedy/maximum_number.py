# Maximum Number
# Leetcode -> 1323. Maximum 69 Number

# You are given a positive integer num consisting only of digits 6 and 9.
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Example 1:
# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.

# Example 2:
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.

# Example 3:
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.

# Constraints
# 1 <= num <= 104
# num consists of only 6 and 9 digits.

# Steps to Solve the Maximum Number Problem
# Here's how to solve the "Maximum Number" problem in a structured approach:
# 1. **Understand the problem**:
#   - We have a number consisting only of 6's and 9's
#   - We can change at most one digit (either 6→9 or 9→6)
#   - Goal: Find the maximum possible number after making at most one change
# 2. **Recognize the key insight**:
#   - To maximize a number, we should change the leftmost (most significant) 6 to a 9
#   - Changing a 9 to a 6 will always decrease the number, so we never want to do that
# 3. **Convert the number to string**:
#   - This makes it easier to examine and modify individual digits
# 4. **Scan the number from left to right**:
#   - Look for the first occurrence of the digit '6'
#   - Once found, change it to '9'
#   - If no '6' is found, keep the original number
# 5. **Convert back to integer**:
#   - After making the change, convert the modified string back to an integer
# 6. **Return the result**:
#   - The new number will be the maximum possible
# The time and space complexity are both O(n), where n is the number of digits in the input number.

# BruteForcce Method
def maximum69Number_brute_force(num):
    # Step 1: Convert number to string for easier digit manipulation
    num_str = str(num)
    
    # Step 2: Try changing each digit and find the maximum
    max_num = num  # Start with original number
    
    for i in range(len(num_str)):
        # Step 3: Create new number by changing current digit
        new_num_str = list(num_str)
        if num_str[i] == '6':
            new_num_str[i] = '9'
        else:  # num_str[i] == '9'
            new_num_str[i] = '6'
        
        # Step 4: Convert back to integer and compare
        new_num = int(''.join(new_num_str))
        max_num = max(max_num, new_num)
    
    # Step 5: Return the maximum number found
    return max_num

# Optimal Method
def maximum69Number_optimized(num):
    # Step 1: Convert number to string
    num_str = str(num)
    
    # Step 2: Find the first occurrence of '6' and replace it
    # (if no 6 exists, return the original number)
    for i in range(len(num_str)):
        if num_str[i] == '6':
            # Replace the first '6' with '9'
            return int(num_str[:i] + '9' + num_str[i+1:])
    
    # Step 3: If no '6' is found, return the original number
    return num