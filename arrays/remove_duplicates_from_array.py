# Remove Duplicates from Sorted Collection

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Imagine you have a collection of numbered cards arranged neatly in a line. Each number represents a unique value, and all the cards with the same number are grouped together because they are sorted. 
# Your task is to find a way to keep only one card of each number and remove the rest, while maintaining the order of numbers. In the end, count how many different numbers you retained in your collection.
# Your objective is to modify the array directly to achieve this without creating a new array. At the end of the process, return the number of unique numbers left in the array.

# Constraints
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.

# ## Step-by-Step Problem-Solving Guide:
# 1. **Understand that the array is already sorted** - this means all duplicates are adjacent to each other
# 2. **Use two pointers** - one to iterate through the array, one to track where to place unique elements
# 3. **Skip over duplicates** - when we find a new unique element, place it at the next position for unique elements
# 4. **Modify in-place** - overwrite the array directly without using extra space
# 5. **Track the count** - the position of the second pointer gives us the count of unique elements
# 6. **Handle edge cases** - like empty arrays
# 7. **Utilize the sortedness** - we only need to compare each element with the previous one
# 8. **Maintain order** - this happens automatically as we process the array from left to right
# 9. **Return the correct count** - the unique_position variable contains the number of unique elements
# 10. **Consider the problem visualization** - think of it as keeping one card of each number in the sorted collection

# BruteForce Method
def removeDuplicates_brute_force(nums):
    # Step 1: If array is empty, return 0
    if not nums:
        return 0
    
    # Step 2: Create a list of unique elements in order
    unique_elements = []
    for num in nums:
        if not unique_elements or num != unique_elements[-1]:
            unique_elements.append(num)
    
    # Step 3: Modify the original array
    for i in range(len(unique_elements)):
        nums[i] = unique_elements[i]
    
    # Step 4: Return the count of unique elements
    return len(unique_elements)

# Approach 2

def removeDuplicates(self, nums):
    if not nums:
        return 0
    uniqueIndex = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[uniqueIndex]:
            uniqueIndex += 1
            nums[uniqueIndex] = nums[i]
    return uniqueIndex + 1

# 2 pointer approach
def removeDuplicates_optimized(nums):
    # Step 1: Handle empty array
    if not nums:
        return 0
    
    # Step 2: Initialize pointer for unique elements position
    unique_position = 1
    
    # Step 3: Iterate through the array starting from second element
    for i in range(1, len(nums)):
        # Step 4: If current element is different from previous one
        if nums[i] != nums[i-1]:
            # Step 5: Place it at the unique_position
            nums[unique_position] = nums[i]
            # Step 6: Increment the unique_position
            unique_position += 1
    
    # Step 7: Return the count of unique elements
    return unique_position