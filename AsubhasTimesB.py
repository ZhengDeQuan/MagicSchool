'''
腾讯笔试题，字符串系数
字符串A的所有不同的子串，在B中出现的次数的和，定义为字符串A，B的系数
比如：A="abab",B="ababab"
A的子串有"ab"、"ba"两种，分别在B中出现了3次和2次，所以系数为3+2=5
'''


def hashStringToNumber(array,k):
    Dict =dict()
    for i in range(len(array) - k+1):
        temp_s = array[i:i+k]
        if temp_s not in Dict:
            Dict[temp_s] = 1
        else:
            Dict[temp_s] += 1
    return Dict


def solve(A,B,k):
    if len(B) < k:
        return 0
    Ad = hashStringToNumber(A,k)
    Bd = hashStringToNumber(B,k)
    res = 0
    for key in Ad:
        if key in Bd:
            res += Bd[key]
    return res


if __name__ == "__main__":
    print(solve('abab',"ababab",2))