# Arrange Sorted Arrays
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input:
# nums1 = [1,2,3,0,0,0], m = 3, 
# nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6].

# Example 2:
# Input:
# nums1 = [1], m = 1, 
# nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and []. The result of the merge is [1].

# Example 3:
# Input:
# nums1 = [0], m = 0, 
# nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1]. The result of the merge is [1]. Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

# Constraints
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[i] <= 10^9

## Step-by-Step Problem-Solving Approach:
# 1. **Understand the problem**: We need to merge two sorted arrays into one, with the result stored in the first array.
# 2. **Identify constraints**: The first array has extra space at the end filled with zeros.
# 3. **Consider standard approaches**: Merging sorted arrays is typically done with a two-pointer technique.
# 4. **Key insight**: Starting from the end avoids overwriting values we still need.
# 5. **Initialize pointers**: One for the end of each array's valid elements, and one for the end of the merged array.
# 6. **Merge backward**: Compare elements and place the larger one at the end of nums1.
# 7. **Handle leftover elements**: Only nums2 might have leftover elements that need to be placed.
# 8. **Check edge cases**: What if one array is empty? The solution handles this automatically.
# 9. **Verify time complexity**: O(m+n) since we process each element once.
# 10. **Test with examples**: Try the solution on the given examples to verify correctness.

# BruteForce Method
def merge_brute_force(nums1, m, nums2, n):
    # Step 1: Add all elements from nums2 to the end of nums1 (replacing zeros)
    for i in range(n):
        nums1[m + i] = nums2[i]
    
    # Step 2: Sort the entire array
    nums1.sort()
    
# Optimized method
def merge_optimized(nums1, m, nums2, n):
    # Step 1: Initialize pointers to the end of each array
    p1 = m - 1  # Last element in nums1
    p2 = n - 1  # Last element in nums2
    p = m + n - 1  # Last position in the final array
    
    # Step 2: Work backwards, placing the larger element at position p
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # Step 3: If there are remaining elements in nums2, add them
    # (Any remaining elements in nums1 are already in their correct place)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1