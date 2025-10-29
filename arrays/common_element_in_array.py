# Find Common Elements in Two Arrays

# Intersection of Two Arrays II
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays, and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Constraints
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


## Step-by-Step Problem-Solving Guide:
# 1. **Understand the problem**: We need to find elements that appear in both arrays, respecting their frequencies.
# 2. **Choose the right approach**: Use a hash map to count frequencies in one array, then check against the other.
# 3. **Optimize for space**: Count frequencies for the smaller array to minimize space usage.
# 4. **Count element frequencies**: Store how many times each number appears in the first array.
# 5. **Build the intersection**: For each element in the second array, check if it's in our counter.
# 6. **Handle duplicates correctly**: Decrement the counter after including an element in the result.
# 7. **Return the result**: The array containing all common elements with correct frequencies.

# BruteForce Method
def intersect_brute_force(nums1, nums2):
    # Step 1: Initialize result array
    result = []
    
    # Step 2: Create a copy of nums2 to mark used elements
    nums2_copy = nums2.copy()
    
    # Step 3: For each element in nums1, look for a match in nums2
    for num in nums1:
        # Step 4: Check if the element exists in nums2_copy
        if num in nums2_copy:
            # Step 5: Add to result and remove from nums2_copy to avoid duplicates
            result.append(num)
            nums2_copy.remove(num)
    
    return result

# Optimized using hash map
def intersect_optimized(nums1, nums2):
    # Step 1: Create a counter for the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # Step 2: Count frequencies in the first array
    counter = {}
    for num in nums1:
        counter[num] = counter.get(num, 0) + 1
    
    # Step 3: Check elements in the second array and build result
    result = []
    for num in nums2:
        # Step 4: If element exists in counter and count > 0, add to result
        if num in counter and counter[num] > 0:
            result.append(num)
            counter[num] -= 1
    
    return result