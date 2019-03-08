# import sys
# sys.stdin  = open('in.txt',"r",encoding="utf-8")

if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        T -=1
        n = int(input())
        numbers = list(map(int,input().split()))
        A = 0
        B = 0
        if n%2 == 0:
            for i in range(n):
                if i %2 ==0:
                    A += numbers[i]
                else:
                    B += numbers[i]
        else:
            mid_index = int(n / 2)
            A += numbers[mid_index]
            for i in range(mid_index):
                if i %2 ==0:
                    A += numbers[i]
                else:
                    B += numbers[i]
            for i in range(mid_index+1,n):
                if i %2 ==0:
                    B += numbers[i]
                else:
                    A += numbers[i]
        print("Case #{}: {} {}".format(i,B,A))



