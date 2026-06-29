"""
3512. Minimum Operations to Make Array Sum Divisible by K

You are given an integer array nums and an integer k. You can perform the following operation any number of times:

Select an index i and replace nums[i] with nums[i] - 1.
Return the minimum number of operations required to make the sum of the array divisible by k.

"""

nums = [3,9,7]
k = 5

def minOperations(nums:list[int], k:int) -> int:
    return sum(nums) % k

print(minOperations(nums, k))
