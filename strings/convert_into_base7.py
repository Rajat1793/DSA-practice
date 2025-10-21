# Convert to Base 7

# Given an integer num, your task is to convert it into its base 7 representation and return it as a string. Base 7 numbers use only the digits 0 through 6. This means that after counting to 6, you move to a new column, similar to how base 10 works after the digit 9.
# For example, when converting a base 10 number like 20 (imagine Hitesh has 20 candies) to base 7, it would be represented as '26'. Similarly, negative numbers should also be correctly represented in base 7.
# The challenge is to convert any integer, positive or negative, into this base 7 form, presented as a string.

# Example 1:
# Input: num = 100
# Output: "202"

# Example 2:
# Input: num = -7
# Output: "-10"

# Your task is to implement a function that performs this conversion accurately.

# Constraints
# num is an integer where -10^7 <= num <= 10^7

# Breaking Down the "Convert to Base 7" Problem

# Let me explain how to tackle this problem step-by-step, with guidance that will help you solve similar problems on your own.

# ## Understanding Base Conversion

# First, let's understand what converting to base 7 means:
# - In base 7, we only use digits 0-6
# - Each position represents a power of 7 (e.g., 7⁰, 7¹, 7², etc.)
# - We need to find these digits through division and remainders

# ## Step-by-Step Approach

# ### 1. Identify Edge Cases
# - What if the number is 0?
# - What if the number is negative?

# ### 2. Develop a General Algorithm
# - Remove the sign (work with absolute value)
# - Repeatedly divide by 7, collecting remainders
# - Read the remainders in reverse order
# - Add the sign if needed

# ### 3. Code Implementation Steps

# ## Example Walkthrough
# Let's trace through the example where num = 100:

# 1. Is num 0? No, continue.
# 2. Is num negative? No, is_negative = False.
# 3. Begin conversion:
#    - num = 100, remainder = 100 % 7 = 2, result = ['2'], num = 100 // 7 = 14
#    - num = 14, remainder = 14 % 7 = 0, result = ['2', '0'], num = 14 // 7 = 2
#    - num = 2, remainder = 2 % 7 = 2, result = ['2', '0', '2'], num = 2 // 7 = 0
# 4. Loop ends when num becomes 0
# 5. Reverse result: ['2', '0', '2'] → "202"
# 6. No negative sign needed
# 7. Return "202"

# ## General Problem-Solving Tips

# 1. **Break down the problem**: Identify the main steps needed
# 2. **Handle special cases first**: Zero and negative numbers often need special handling
# 3. **Use descriptive variable names**: Makes your code easier to understand
# 4. **Test your solution**: Try with provided examples and edge cases
# 5. **Consider different approaches**: Is there a more efficient way to solve it?

# By following this methodical approach, you can tackle not just base conversion problems, but many other algorithmic challenges as well.

def convertToBase7(num):
    # Step 1: Handle the zero case first
    if num == 0:
        return "0"
    
    # Step 2: Handle the sign
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)  # Work with absolute value
    
    # Step 3: Perform the base conversion
    result = []
    while num > 0:
        # Get remainder when divided by 7
        remainder = num % 7
        
        # Add the remainder to our results
        result.append(str(remainder))
        
        # Integer division by 7 for next iteration
        num //= 7
    
    # Step 4: Construct the final string
    # (Remainders need to be read in reverse order)
    base7 = ''.join(reversed(result))
    
    # Step 5: Add the negative sign if needed
    if is_negative:
        base7 = '-' + base7
    
    return base7

# bruteforce method
def convertToBase7_brute_force(num):
    # Step 1: Handle the special case of 0
    if num == 0:
        return "0"
    
    # Step 2: Handle negative numbers
    is_negative = num < 0
    num = abs(num)  # Work with absolute value
    
    # Step 3: Convert to base 7 by repeatedly dividing by 7
    result = ""
    while num > 0:
        remainder = num % 7
        result = str(remainder) + result
        num = num // 7
    
    # Step 4: Add negative sign if needed
    if is_negative:
        result = "-" + result
    
    return result