
def firstBadVersion(n):
    left = 1
    right = n

    while(left < right):
        mid = left + (right - left) / 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

nums = [-1,0,3,5,9,12]
target = 9
output = firstBadVersion(nums)
print(output)
