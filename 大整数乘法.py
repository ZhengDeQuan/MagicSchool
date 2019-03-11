

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1)== 1 and num1 == '0' or len(num2) == 1 and num2 == '0':
            return '0'
        num1 = [int(ch) for ch in num1]
        num2 = [int(ch) for ch in num2]
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        max_length = 0
        for i in range(0 , len(num1)):
            for j in range(0 , len(num2)):
                if i+j > max_length:
                    max_length = i + j
                res[i+j] += num1[i] * num2[j]

        for i in range(0 , max_length+1):
            if res[i] >=10 :
                res[i+1] += int( res[i]/10 )
                res[i] = res[i]%10

        i = max_length + 1
        while res[i] >= 10:
            if i + 1>= len(res):
                max_length+=1
                res.append(0)
            res[i+1] += int(res[i]/10)
            res[i] = res[i]%10
        max_length = i
        while max_length < len(res) and res[max_length] > 0:
            max_length += 1
        res = res[:max_length][::-1]
        res = list(map(str,res))
        return ''.join(res)

if __name__ == "__main__":
    A = Solution()
    res = A.multiply('408','5')
    print("res= ",res)