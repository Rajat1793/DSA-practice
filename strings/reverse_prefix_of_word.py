# Reverse Prefix of Word

# You are given a 0-indexed string word and a character ch. Your task is to reverse the segment of word starting at index 0 and ending at the index of the first occurrence of ch (inclusive). If ch does not exist in the word, leave the word unchanged.

# For example, if word = "abcdefd" and ch = "d", the segment from index 0 to 3 (inclusive) is reversed, resulting in the string "dcbaefd".

# Return the modified string after performing the described operation.

# Example 1:
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. Reverse the segment from 0 to 3, resulting in "dcbaefd".

# Example 2:
# Input: word = "xyxzxe", ch = "z"
# Output: "zxyxxe"
# Explanation: The first occurrence of "z" is at index 3. Reverse the segment from 0 to 3, resulting in "zxyxxe".

# Example 3:
# Input: word = "abcd", ch = "z"
# Output: "abcd"
# Explanation: The character "z" does not exist in the word, so no reversal occurs. The word remains "abcd".

# This challenge encourages you to manipulate strings by identifying the first occurrence of a character and selectively reversing parts of the string based on that position.

# Constraints
# The length of the word (n) is in the range 1 <= n <= 100.
# The character ch is a single lowercase letter.

# BruteForce method
def flipStartOfWord(self, word: str, ch: str) -> str:
        '''
        word: string representing the word
        ch: character to find in the word
        Returns: the modified string after performing the described operation
        '''
        # Find the first occurrence of ch
        ch_index = -1
        for i in range(len(word)):
            if word[i] == ch:
                ch_index = i
                break
        
        # If ch is not found, return the original word
        if ch_index == -1:
            return word
        
        # Reverse the prefix from index 0 to ch_index (inclusive)
        prefix = word[:ch_index + 1]
        reversed_prefix = prefix[::-1]
        
        # Return the reversed prefix concatenated with the rest of the word
        return reversed_prefix + word[ch_index + 1:]

# Optimized way
def reversePrefix_optimized(word, ch):
    # Find the index of the first occurrence of ch
    if ch not in word:
        return word
    
    ch_index = word.find(ch)
    
    # Convert the word to a list for in-place operations
    word_list = list(word)
    
    # Reverse the segment from index 0 to ch_index
    left, right = 0, ch_index
    while left < right:
        word_list[left], word_list[right] = word_list[right], word_list[left]
        left += 1
        right -= 1
    
    # Convert back to a string and return
    return ''.join(word_list)
    
