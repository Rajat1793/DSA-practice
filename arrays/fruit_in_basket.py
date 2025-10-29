# Fruits Allocation in Baskets
# leetCode --> 3477. Fruits Into Baskets II
# leetCode --> 3479. Fruits Into Baskets III

# You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
# From left to right, place the fruits according to these rules:

# Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
# Each basket can hold only one type of fruit.
# If a fruit type cannot be placed in any basket, it remains unplaced.
# Return the number of fruit types that remain unplaced after all possible allocations are made.


# Example 1:
# Input: fruits = [4,2,5], baskets = [3,5,4]
# Output: 1
# Explanation:
# fruits[0] = 4 is placed in baskets[1] = 5.
# fruits[1] = 2 is placed in baskets[0] = 3.
# fruits[2] = 5 cannot be placed in baskets[2] = 4.
# Since one fruit type remains unplaced, we return 1.

# Example 2:
# Input: fruits = [3,6,1], baskets = [6,4,7]
# Output: 0
# Explanation:
# fruits[0] = 3 is placed in baskets[0] = 6.
# fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
# fruits[2] = 1 is placed in baskets[1] = 4.
# Since all fruits are successfully placed, we return 0.


# Constraints:
# n == fruits.length == baskets.length
# 1 <= n <= 105
# 1 <= fruits[i], baskets[i] <= 109

def unplacedFruits_BruteForce(fruits: list[int], baskets: list[int]) -> int:
    """
    Brute Force Approach
    Time: O(n²) - for each fruit, we may scan all baskets
    Space: O(n) - for the used array
    """
    n = len(fruits)
    used = [False] * n  # Track which baskets are occupied
    unplaced_count = 0
    
    # Process each fruit TYPE from left to right
    for fruit_quantity in fruits:
        placed = False
        
        # Scan ALL baskets from left to right (LEFTMOST FIRST)
        for basket_index in range(n):
            # Check if this basket is available AND has enough capacity
            if not used[basket_index] and baskets[basket_index] >= fruit_quantity:
                used[basket_index] = True  # Mark as used
                placed = True
                break  # Stop searching, found the leftmost available
        
        # If no suitable basket was found
        if not placed:
            unplaced_count += 1
    
    return unplaced_count

# other approach
def unplacedFruits_Optimized(fruits: list[int], baskets: list[int]) -> int:
        '''
        fruits: List[int] - list of integers representing the quantity of each type of fruit
        baskets: List[int] - list of integers representing the capacity of each basket
        '''
        unplacedFruits = 0
        
        # Sort fruits and baskets in non-decreasing order
        fruits.sort()
        baskets.sort()
        
        basketIndex = 0
        
        for fruit in fruits:
            # Find the first basket that can hold the fruit
            while basketIndex < len(baskets) and baskets[basketIndex] < fruit:
                basketIndex += 1

            if basketIndex < len(baskets):
                # Place the fruit in the basket
                basketIndex += 1
            else:
                # Could not place the fruit in any basket
                unplacedFruits += 1

        return unplacedFruits