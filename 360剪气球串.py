# import sys
# sys.stdin = open("in.txt","r",encoding="utf8")
mod = 1000000007
MAX = 100000+5



if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int,input().split()))
    #print(numbers)
    dp = [0] * (n+1)
    dp[0]=1

    for i in range(1,n+1):
        count = [0] * 10
        for j in range(1,min(i+1,9)):
            count[numbers[i-j]] += 1
            if count[numbers[i-j]] > 1:
                break

            dp[i] = (dp[i] + dp[i - j]) % mod
            #print("i = ",i," j = ",j , " v = ",dp[i])
    print(dp[n])