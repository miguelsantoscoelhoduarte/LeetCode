
'''
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :rtype: List[int]
    """
	numbers_len = len(numbers)
	res_list = list()
	i, j = 0, numbers_len-1
	while i<j:
		if numbers[i] + numbers[j] == target:
			res_list.append(i+1)
			res_list.append(j+1)
			return res_list
		elif numbers[i] + numbers[j] < target:
			i+=1
		elif numbers[i] + numbers[j] > target:
			j-=1

ums = [1,2,3,4,4,9,56,90]
target = 8
output = twoSum(nums,  target)
print(output)
