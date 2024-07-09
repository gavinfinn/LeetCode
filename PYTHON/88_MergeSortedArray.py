class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        endIndex = m + n - 1
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[endIndex] = nums1[m - 1]
                m -= 1
            else:
                nums1[endIndex] = nums2[n - 1]
                n -= 1
            endIndex -= 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
solution = Solution()
solution.merge(nums1, 3, nums2, 3)
print(nums1)