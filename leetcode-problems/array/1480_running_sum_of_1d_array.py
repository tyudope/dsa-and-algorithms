"""
1480. Running Sum Of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

"""


def runningSum(nums:list[int]) -> list[int]:

    for i in range(1, len(nums)):
        nums[i] += nums[i-1]

    return nums


nums = [1,2,3,4]
print(f"Running sum of {nums} is equal to = {runningSum(nums)}")
assert runningSum([1,2,3,4]) == [1,3,6,10]



"""
Approach: 
    In-place prefix sum - each element accumulates the one before it.


Time: O(n) - single pass over time.
Space: O(1) - mutate nums in place, no extra structure.


"""