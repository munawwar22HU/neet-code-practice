class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # frequencyCounter = dict()
        # for n in nums:
        #     frequencyCounter[n] = frequencyCounter.get(n,0)+1
        # sortedCounter = sorted(frequencyCounter.items(), key= lambda x: x[1], reverse=True)
        # result = [k for k,v in sortedCounter[:k]]
        # return result

       
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

