class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
        result = ''
        reverse = len(s)
        for i in range(len(s)):
            if s[i] in vowels:
                reverse -= 1
                while s[reverse] not in vowels:
                    reverse -= 1
                result += s[reverse]
            else:
                result += s[i]
        return result
                    
s = "leetcode"
solution = Solution()
print(solution.reverseVowels(s))