

if __name__ == "__main__":
    T = int(input())
    for case_num in range(1,T+1):
        R,C,K = list(map(int,input().split()))
        unK = R * C - K
        if unK == 1:
            print('Case #%d: IMPOSSIBLE'%(case_num))
        else:
            print('Case #%d: POSSIBLE'%(case_num))
            ret = ""
            if R * C == 1:
                print("S")
            elif R == 1: # [] [] [] [] []
                ret = "E"
                unK -= 1
                ret += unK * "W"
                ret += (C - unK - 1) * "N"
                ret += "\n"
            elif C == 1:
                '''
                []
                []
                []
                []
                '''
                ret = "S\n"
                unK -=1
                ret += unK*("N\n")
                ret += (R-unK-1) * ("E\n")
            else:
                while unK >= C:
                    ret += "E" + (C-1) * 'W' + "\n"
                    unK -= C
                    R -= 1
                if unK:
                    if unK == 1:
                        ret += 'N'
                    else:
                        ret += 'E' + "W"*(unK-1 )
                    ret += 'S'*(C-unK)+"\n"
                    R-=1
                if R:
                    ret += ("S"*C+"\n")*R
            print(ret)
