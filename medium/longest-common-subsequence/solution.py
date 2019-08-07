class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_1, len_2 = len(text1), len(text2)
        dp = [[0] * (len_1 + 1) for _ in range(len_2 + 1)]
        for i in range(len_2):
            for j in range(len_1):
                if text1[j] == text2[i]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]