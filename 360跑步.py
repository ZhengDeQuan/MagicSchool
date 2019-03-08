# import sys
import math
# sys.stdin = open("in.txt","r",encoding="utf8")

if __name__ == "__main__":
    L,R = list(map(int,input().split()))
    theta = L / R
    X = math.cos(theta) * R
    Y = math.sin(theta) * R
    print("%.3f %.3f"%(X,-Y))
    print("%.3f %.3f"%(X,Y))

