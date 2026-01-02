class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        # """

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')]+=1
                
            res[tuple(count)].append(s)

        return res.values()

        # hashMap = dict()

        # for s in strs:
        #     counter = (Counter(s))
        #     if counter not in hashMap:
        #         hashMap[counter] = [s]
        #     else:
        #         hashMap[counter].append(s)
        # return list(hashMap.values())

        # anagrams = dict()
        # for s in strs:
        #     val = tuple(sorted(s))
        #     if val in anagrams:
        #         anagrams[val].append(s)
        #     else:
        #         anagrams[val] = [s]
        # return list(anagrams.values())


      
            

            

        


                
                
        

            
            
