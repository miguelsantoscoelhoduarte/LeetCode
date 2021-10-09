
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    amountNumsSmallerThanTarget = 0

    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif target > nums[i]:
            amountNumsSmallerThanTarget = amountNumsSmallerThanTarget + 1
    return amountNumsSmallerThanTarget

nums = [1,3,5,6]
target = 7
output = searchInsert(nums, target)
print(output)
