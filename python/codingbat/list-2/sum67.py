# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
# extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
#
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(nums):
    for num in nums:
        currIndex = nums.index(num)

        if num == 6:
            nums[currIndex] = 0
            index = currIndex
            for index in range(currIndex,len(nums) - 1):
                if nums[index + 1] is not 7:
                    nums[index] = 0
                elif nums[index + 1] is 7:
                    nums[index] = 0
                    nums[index + 1] = 0
                    break
            
    return sum(nums)  
