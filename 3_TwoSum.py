class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
 #    n = len(nums)
    #    for i in range(n):
    #         for j in range(i+1,n):
    #             if nums[i] + nums[j] == target:
    #                 return [i,j] if i < j else [j,i]

        hashIndex = {}

        for index,value in enumerate(nums):
            if target - value not in hashIndex:
                hashIndex[value] = index
            else:
                return [hashIndex[target-value],index]
            
        
            
