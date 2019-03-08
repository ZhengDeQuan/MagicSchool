class Solution:
    def canWin(self,maxChooseableInterger , desiredTotal , used):
        if used in self.dp:
            return self.dp[used]
        for i in range(maxChooseableInterger):
            cur = 1 << i
            if not (used & cur):
                if (i+1) >= desiredTotal or not self.canWin(maxChooseableInterger,desiredTotal-(i+1),used | cur):
                    self.dp[used] = True
                    return True
        self.dp[used] = False
        return False


    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger >= desiredTotal:
            return True
        elif maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False
        else:
            self.dp = dict()
            if self.canWin(maxChoosableInteger ,desiredTotal , 0):
                return True
            else:
                return False


if __name__ == "__main__":
    A = Solution()
    res = A.canIWin(10,11)
    print("res = ",res)