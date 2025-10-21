# Find Most Frequent Vowels and Consonants

# You are given a string s consisting of lowercase English letters ('a' to 'z').
# Your task is to:
# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.
# The frequency of a letter x is the number of times it occurs in the string.

# Example 1:
# Input: s = "treetops"
# Output: 4
# Explanation:
# The vowels are: 'e' (frequency 2), 'o' (frequency 1). The maximum frequency is 2.
# The consonants are: 't' (frequency 2), 'r' (frequency 1), 'p' (frequency 1), 's' (frequency 1). The maximum frequency is 2.
# The output is 2 + 2 = 4.

# Example 2:
# Input: s = "ooeeaa"
# Output: 3
# Explanation:
# The vowels are: 'o' (frequency 2), 'e' (frequency 2), 'a' (frequency 2). Any one can be chosen as the maximum frequency which is 2.
# There are no consonants in `s`. Hence, maximum consonant frequency = 0.
# The output is 2 + 0 = 2.

# Example 3:
# Input: s = "fffffff"
# Output: 7
# Explanation:
# There are no vowels in `s`. Hence, maximum vowel frequency = 0.
# The consonant is: 'f' (frequency 7). Thus, its maximum frequency is 7.
# The output is 0 + 7 = 7.

# Constraints
# 1 <= length of s <= 1000
# s consists of only lowercase English letters ('a' to 'z')

# BruteForce Method
def maxFreqSum_brute_force(s):
    vowels = 'aeiou'
    letter_count = {}
    for char in s:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    # Find maximum vowel frequency
    max_vowel_freq = 0
    for char in letter_count:
        if char in vowels and letter_count[char] > max_vowel_freq:
            max_vowel_freq = letter_count[char]
    
    # Find maximum consonant frequency
    max_consonant_freq = 0
    for char in letter_count:
        if char not in vowels and letter_count[char] > max_consonant_freq:
            max_consonant_freq = letter_count[char]
    
    # Return sum of maximum frequencies
    return max_vowel_freq + max_consonant_freq

# optimized method using single pass through
def maxFreqSum_optimized(s):
    # Define vowels
    vowels = set('aeiou')
    
    # Dictionaries to store frequencies
    vowel_freq = {}
    consonant_freq = {}
    
    # Count frequencies in a single pass
    for char in s:
        if char in vowels:
            vowel_freq[char] = vowel_freq.get(char, 0) + 1
        else:
            consonant_freq[char] = consonant_freq.get(char, 0) + 1
    
    # Find maximum frequencies
    max_vowel_freq = max(vowel_freq.values()) if vowel_freq else 0
    max_consonant_freq = max(consonant_freq.values()) if consonant_freq else 0
    
    return max_vowel_freq + max_consonant_freq

print(maxFreqSum_brute_force("treetops"))
print(maxFreqSum_optimized("treetops"))

# most optimized
class Solution:
    def maxFreqSum(self, s: str) -> int:
        con = 0
        vow = 0
        d_set = set(s)
        for i in d_set:
            if i in "aeiou":
                vow = max(vow, s.count(i))
            else:
                con = max(con, s.count(i))
        return con+vow 