"babgbag"
"bag"
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        length_s = len(s)
        length_t = len(t)
        if length_s == 0:
            if length_t == 0:
                return 1
            else:
                return 0
        elif length_t == 0:
            return 1
        dp = [[0] * ( length_s + 1 ) for i in range(length_t+1)]
        #dp[i][j] 长度为i的字串在长度为j的母串中出现的次数
        dp[0][0] = 1
        for j in range(length_s + 1):
            dp[0][j] = 1
        for i in range(1,length_t+1):
            for j in range(1,length_s+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        # print("dp = ")
        # for line in dp:
        #     print(line)
        return dp[length_t][length_s]

if __name__ == "__main__":
    A = Solution()
    s = "babgbag"
    t = "bag"
    res = A.numDistinct(s,t)
    print("res= ",res)
