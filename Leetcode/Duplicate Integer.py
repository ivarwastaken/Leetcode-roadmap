'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
'''

'''
Answer:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        nums.sort()
        for n in range(len(nums)):
            if nums[n-1] == nums[n]:
                return True
        return False
'''
    