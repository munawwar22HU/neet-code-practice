class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for s in strs:
            new_string += str(len(s))+"#"+s
        return new_string

    def decode(self, s: str) -> List[str]:
        output_list = []
        n = len(s)
        length_index = 0
        l = ""
        word = ""
        while length_index<n:
            for x in range(length_index,n):
                if s[x]=="#":
                    break
                else:
                    l+=s[x]
            start = length_index+len(l)+1
            end = start + int(l)
            word = s[start:end]
            output_list.append(word)
            length_index = end
            l = ""
        return output_list
            

        


