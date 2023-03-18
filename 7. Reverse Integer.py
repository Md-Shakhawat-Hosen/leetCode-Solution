class Solution(object):
    # def foundReverse(self,x):
    #     s = 0
    #     while x != 0:
    #         r = x % 10
    #         s = s * 10 + r
    #         x = x // 10
    #     return s
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = int(str(x)[::-1]) if x >= 0 else -int(str(x)[1:][::-1])
        if -2**31 <= res <=(2**31)-1:
            return res
        else:
            return 0
        # if x < 0:
        #     s = str(x)
        #     a = ""
        #     for i in range(1,len(s)):
        #         a = a + s[i]
        #     r = Solution()
        #     result = r.foundReverse(int(a))
        #     if result > (2**31):
        #         return 0
        #     else:
        #         return -result
        # else:
        #     r = Solution()
        #     result = r.foundReverse(x)
        #     if result > (2**31)-1:
        #         return 0
        #     else:
        #         return result


myobj = Solution()
x = -1200
r = myobj.reverse(x)
print(r)