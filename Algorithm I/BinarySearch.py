
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
    
nums = [-1,0,3,5,9,12]
target = 9
output = search(nums, target)
print(output)

nums = [-1,0,3,5,9,12]
target = 2
output = search(nums, target)
print(output)
