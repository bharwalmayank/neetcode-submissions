class Solution:
    
    def encode(self, strs: List[str]) -> str:
        # use a tuple with index as key rep alphabets and value as frequency
        enc = ""
        for w in strs:
            l = len(w)
            enc += f"{l}#" + w

        return enc

    def decode(self, s: str) -> List[str]:

        # at each decoding step, we must know, the index of the payload(including delimiters), 
        # the len to read
        # and the ind of len

        p_ind, length, l_ind = 0, float('-inf'), 0
        res = []

        while p_ind < len(s):

            while s[l_ind] != '#':
                l_ind += 1
            length = int(s[p_ind:l_ind])

            word = s[l_ind+1:l_ind+1+length]
            res.append(word)
            p_ind = l_ind + 1 + length
            l_ind = p_ind

        return res
