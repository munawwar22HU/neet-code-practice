class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        """ # Sorted Solution
        return sorted(s) == sorted(t)
        """

        """ # Counter Solution
        # return Counter(s) == Counter(t)
        """


        ''' # Hashmap Solution 
        if len(s) != len(t):
            return False
        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True '''
        



        

        dict1 = dict()
        dict2 = dict()

        for char in s:
            dict1[char] = dict1.get(char,0) + 1
        
        for char in t:
            dict2[char] = dict2.get(char,0) + 1
        
        for key in dict1:
            if key not in dict2:
                return False
        for key in dict2:
            if key not in dict1:
                return False
        for key in dict1:
            if dict1[key] != dict2[key]:
                return False
        return True         
