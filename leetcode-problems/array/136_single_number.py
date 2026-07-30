"""136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one.
 Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""


def singleNumber(nums:list[int]) -> int:

    seen = {}
    for num in nums:
        if num in seen:
            seen[num] += seen.get(num, 1)
        else:
            seen.setdefault(num, 1)
    for key, value in seen.items():
        if value == 1:
            return key
    


nums = [1,2,2,3,3]
print(singleNumber(nums))
    