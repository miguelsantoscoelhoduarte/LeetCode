
'''
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def moveZeroes(nums):
    pointer = None

    for i in range(len(nums)):
        if nums[i] == 0 and pointer == None:
            pointer = i

        if nums[i] != 0 and i != 0 and pointer != None:
            print(i,"entrei")
            #print(nums[pointer], nums[i])
            nums[pointer] = nums[i]
            nums[i] = 0
            pointer += 1
        #print(nums)

    return nums

nums = [0,1,0,3,12]
output = moveZeroes(nums)
print(output)
