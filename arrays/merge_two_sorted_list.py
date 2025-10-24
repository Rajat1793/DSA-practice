# Merge Two Sorted Lists

# You are given two integer arrays arr1 and arr2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in arr1 and arr2 respectively.

# Merge arr1 and arr2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array arr1. To accommodate this, arr1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. arr2 has a length of n.

# Example 1:
# Input: arr1 = [1,2,3,0,0,0], m = 3, arr2 = [2,5,6], n = 3
# Output: arr1 = [1,2,2,3,5,6]
# Explanation: The function should merge arrays such that final sorted array becomes [1,2,2,3,5,6]

# Example 2:
# Input: arr1 = [1], m = 1, arr2 = [], n = 0
# Output: arr1 = [1]
# Explanation: Since arr2 is empty, arr1 remains as [1].

# Example 3:
# Input: arr1 = [0], m = 0, arr2 = [1], n = 1
# Output: arr1 = [1]
# Explanation: Initially all elements of arr1 are 0, hence after merging arr1 becomes [1].

# Constraints
# 1 <= m, n <= 200
# 0 <= arr1[i], arr2[j] <= 10^4
# arr1.length == m + n

## Step-by-Step Problem-Solving Approach:
# 1. **Understand the problem structure**: We have two sorted arrays, and we need to merge them in-place in the first array.
# 2. **Identify the key insight**: Since arr1 has extra space at the end, we can work from the back to avoid overwriting values.
# 3. **Initialize three pointers**:
#   - One for the last valid element in arr1
#   - One for the last element in arr2
#   - One for the last position in the final merged array
# 4. **Compare elements from the back**: Place the larger element at the end of arr1.
# 5. **Move pointers accordingly**: After placing an element, move the corresponding pointer.
# 6. **Handle remaining elements**: If elements remain in arr2, copy them to arr1.
# 7. **No need to handle remaining elements in arr1**: They're already in the correct position.
# 8. **Validate with examples**: Test the solution with the provided test cases.

# BruteForce Method
def merge_brute_force(arr1, m, arr2, n):
    # Step 1: Copy elements from arr2 to the end of arr1
    for i in range(n):
        arr1[m + i] = arr2[i]
    
    # Step 2: Sort the entire array
    arr1.sort()
    
def merge_optimized(arr1, m, arr2, n):
    # Step 1: Initialize pointers to the end of each array's valid elements
    p1 = m - 1  # Pointer to the last element in arr1
    p2 = n - 1  # Pointer to the last element in arr2
    p = m + n - 1  # Pointer to the last position in the final array
    
    # Step 2: Work backwards, placing larger elements at the end
    while p1 >= 0 and p2 >= 0:
        if arr1[p1] > arr2[p2]:
            arr1[p] = arr1[p1]
            p1 -= 1
        else:
            arr1[p] = arr2[p2]
            p2 -= 1
        p -= 1
    
    # Step 3: If there are remaining elements in arr2, copy them
    # (Note: remaining elements in arr1 are already in correct place)
    while p2 >= 0:
        arr1[p] = arr2[p2]
        p2 -= 1
        p -= 1