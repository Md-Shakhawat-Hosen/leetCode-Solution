class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        for item in digits:
            s = s + str(item)
        v = int(s) + 1
        v = str(v)
        digits = list(map(int,v))
        return  digits


digits = [9]
myObj = Solution()
r = myObj.plusOne(digits)
print(r)