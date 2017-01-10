class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i, -1, -1):
                print(str(dp[j]) + " " + s[j:i+1])
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        print(dp)
        return dp[n]


if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", {"leet", "code", "def"}))