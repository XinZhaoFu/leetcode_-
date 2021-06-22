class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool
        """
        if len(astr) <= 1:
            return True
        if len(astr) > 26:
            return False

        mark = 0
        for ch in astr:
            cur_mark = 1 << (ord(ch) - ord('a'))
            if mark & cur_mark != 0:
                return False
            else:
                mark |= cur_mark
        return True
