class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        s1_dict, s2_dict = {}, {}

        for ch in s1:
            s1_dict[ch] = s1_dict.get(ch, 0) + 1

        for ch in s2:
            s2_dict[ch] = s2_dict.get(ch, 0) + 1


        return s1_dict == s2_dict
