class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        s = sorted(strs,key=len)
        l = min(strs,key=len)

        for i in range(len(l)):
            if (s[0][i] != s[-1][i]):
                return ans
            ans += s[0][i]
        return ans



my = Solution()
strs = ["flower","flight","flow"]

r = my.longestCommonPrefix(strs)
print(r)