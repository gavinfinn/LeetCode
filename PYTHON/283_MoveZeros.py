class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            elif nums[j] == 0:
                continue
            elif nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                

nums = [0,1,0,3,12]
solution = Solution()
solution.moveZeroes(nums)
print(nums)