class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """  
        # Brute Force
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False """

        """ # Sorting
        sorted_nums = sorted(nums)
        n = len(nums)
        for i in range(n-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True

        return False """

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



