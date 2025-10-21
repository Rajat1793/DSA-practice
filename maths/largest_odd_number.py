# Largest Odd Number in a String

# Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.

# The number returned should not have leading zero's. But the given input string may have leading zero. (If no odd number is found, then return empty string.)

# Examples:
# Input : s = "5347"
# Output : "5347"
# Explanation :
# The odd numbers formed by given strings are --> 5, 3, 53, 347, 5347.
# So the largest among all the possible odd numbers for given string is 5347.

# Input : s = "0214638"
# Output : "21463"
# Explanation :
# The different odd numbers that can be formed by the given string are --> 1, 3, 21, 63, 463, 1463, 21463.

# We cannot include 021463 as the number contains leading zero.
# So largest odd number in given string is 21463.

# BruteForce method
def largestOddNumber_brute_force(s):
    # Remove leading zeros from the string
    s = s.lstrip('0')
    if not s:
        return ""  
    max_odd = ""
    n = len(s)
    # Generate all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            
            # Skip substrings with leading zeros (except single digit '0')
            if substring[0] == '0' and len(substring) > 1:
                continue
                
            # Check if the number is odd
            if int(substring) % 2 == 1:
                # Update max_odd if current substring is larger
                if not max_odd or int(substring) > int(max_odd):
                    max_odd = substring
    
    return max_odd

# optimized method by checking the odd number from right
def largeOddNum(s):
    ind = -1
    
    # Iterate through the string from the end to beginning
    for i in range(len(s) - 1, -1, -1):
        # Break if an odd digit is found
        if (int(s[i]) % 2) == 1:
            ind = i
            break
    
       # Skipping any leading zeroes
    i = 0
    while i <= ind and s[i] == '0':
        i += 1
    
    # Return the largest odd number substring
    return s[i:ind + 1]
print(largeOddNum("0032579"))
print(largestOddNumber_brute_force("0032579"))

# most optimized 
def largestOddNumber(self, num: str) -> str:
    n=len(num)
    for i in range(n-1,-1,-1):
        if num[i] in "13579":
            return num[:i+1]
    return ""