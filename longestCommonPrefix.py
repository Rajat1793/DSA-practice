# Finding the Longest Common Starting Letters
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["windtalker","windy","wind"]
# Output: "wind"

# Example 2:
# Input: strs = ["cat","dog","elephant"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

# BrutForce Method
def longestCommonPrefix(strs):
    if not strs:
        return ""
    min_length = min(len(s) for s in strs) #length of the string
    # checking character position
    for i in range(min_length):
        char = strs[0][i]  # Character to compare with
        # Check if this character is the same in all strings
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return strs[0][:i]  # Return prefix up to this point
    # If we get here, the entire shortest string is the common prefix
    return strs[0][:min_length]

# Optimized method Divide and conqure
def longestCommonPrefix_optimized(strs):
    if not strs:
        return ""
    def commonPrefix(s1, s2):
        """Find the common prefix of two strings."""
        i = 0
        while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
            i += 1
        return s1[:i]
    def divideAndConquer(strs, start, end):
        """Find common prefix using divide and conquer."""
        if start == end:
            return strs[start]
        mid = (start + end) // 2
        prefix1 = divideAndConquer(strs, start, mid)
        prefix2 = divideAndConquer(strs, mid + 1, end)
        return commonPrefix(prefix1, prefix2)
    return divideAndConquer(strs, 0, len(strs) - 1)

print(longestCommonPrefix(["windtalker","windy","wind"]))
print(longestCommonPrefix_optimized(["windtalker","windy","wind"]))