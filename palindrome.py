class Solution(object):
    def isPalindrome(self, x):
        flag = False
        if x < 0:
            return flag
        else:
            s = 0
            while x != 0:
                r = x % 10
                s = s*10 + r
                x = x // 10
            return s



n = int(input("x = \n"))
myObj = Solution()
result = myObj.isPalindrome(n)

if result == n:
    print("true")
else:
    print("false")