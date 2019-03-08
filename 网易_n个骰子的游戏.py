
def gcd(a , b):
    if a < b:
        a , b = b ,a
    while a %b != 0:
        a , b = b , a%b
    return b

if __name__ == "__main__":
    n,x = list(map(int , input().split()))
    count_now = [0] * (6*n+1)
    count_pre = [0] * (6*n+1)
    for i in range(1, 6+1):
        count_pre[i] = 1

    for diceNum in range(2,n+1):
        for i in range(1,diceNum+1):
            count_now[i]=0
        for i in range(diceNum,diceNum*6+1):
            for j in range(1,min(i,6+1)):
                count_now[i] += count_pre[i-j]
        count_pre , count_now = count_now , count_pre
    #O(6 * n^2)
    count_pre, count_now = count_now, count_pre
    total = 6 ** n
    sum_method = 0
    for i in range(x , 6*n+1):
        sum_method += count_now[i]

    divider = gcd(total, sum_method)
    if sum_method == 0:
        print(0)
    elif sum_method == total:
        print(1)
    else:
        print(int(sum_method / divider) , end="")
        print("/",end="")
        print(int(total / divider))

