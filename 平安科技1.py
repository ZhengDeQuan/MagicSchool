import sys

sys.stdin = open("in.txt","r")

if __name__ == "__main__":
    s = input()
    s = s.split()
    s = [ele.strip() for ele in s if len(ele.strip()) > 0]
    s = s[::-1]
    print(s)
