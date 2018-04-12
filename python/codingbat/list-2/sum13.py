# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
# so it does not count and numbers that come immediately after a 13 also do not count.
#
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(nums):
    for num in nums:
        currIndex = nums.index(num)
    
    if num == 13:
        nums[currIndex] = 0
        if currIndex is not len(nums) - 1:
            nums[currIndex + 1] = 0
        
    return sum(nums)
