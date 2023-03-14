class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[-(i + 1)] = nums2[i]  # using (-) cause we know only zero in the back that we dont need
        # nums1.sort()
        # print(nums1)
        # Runtime: 51 ms, faster than 45.07% of Python3 online submissions for Merge Sorted Array.
        # Memory Usage: 13.9 MB, less than 97.84% of Python3 online submissions for Merge Sorted Array.
        class Solution:
            def merge(self, nums1, m, nums2, n):
                p, i, j = m + n - 1, m - 1, n - 1
                while j >= 0 and i >= 0:
                    if nums1[i] >= nums2[j]:
                        nums1[p] = nums1[i]
                        i -= 1
                    else:
                        nums1[p] = nums2[j]
                        j -= 1
                    p -= 1
                if j >= 0:
                    while j >= 0:
                        nums1[p] = nums2[j]
                        j -= 1
                        p -= 1




myobj = Solution()
nums1 = [1]
m = 1
nums2 = []
n = 0
myobj.merge(nums1,m,nums2,n)