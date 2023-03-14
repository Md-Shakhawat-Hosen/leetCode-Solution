class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = list(s.strip().split(" "))
        return len(li[-1])





myobj = Solution()
s = "   fly me   to   the moon  "
r = myobj.lengthOfLastWord(s)
print(r)