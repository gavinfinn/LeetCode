class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):            
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) -1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False

flowerbed = [1,0,0,1]
n = 1
solution = Solution()
print(solution.CanPlaceFlowers(flowerbed, n))
