class Solution:
    def greatestNumberofCandies(self, candies: list, extra: int)->list:
        result = []
        for i in range(len(candies)):
            if candies[i] + extra >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result

candies = [2,3,5,1,3]
extraCandies = 3
solution = Solution()
print(solution.greatestNumberofCandies(candies, extraCandies))
