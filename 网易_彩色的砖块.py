# -*- coding:utf-8 -*-

if __name__ == "__main__":
    s = input()
    List = []
    flag = True
    for ch in s:
        if ch not in List:
            List.append(ch)
        if len(List) > 2:
            print(0)
            flag = False
            break
    if flag:
        print(len(List))