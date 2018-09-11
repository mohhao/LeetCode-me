class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        searchNum = {}
        for index, num in enumerate(nums):
            if num in searchNum:
                return [searchNum[num], index]
            searchNum[target - num] = index #逆转字典，实质是hash