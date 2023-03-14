class Solution():
    def strStr(self,haystack,needle):
        a = len(haystack)
        b = len(needle)
        if a < b:
            return -1
        elif a == b:
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(len(haystack)):
            if haystack[i:b+i] == needle:
                return i
        return -1
        #return haystack.find(needle)


haystack = "butsadbutsad"
needle = "sad"
myObj = Solution()
r = myObj.strStr(haystack,needle)
print(r)


