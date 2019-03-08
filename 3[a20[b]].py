# -*- coding:utf-8 -*-
import json

def getCompleteString(array:str)->str:
    List = []
    for ch in array:
        if ch.isalpha():
            List.append(ch)
        elif ch.isdigit():
            List.append(ch)
        elif '[' == ch:
            List.append(ch)
        elif ']' == ch:
            temp_char = ""
            temp_char_number = ""
            while List[-1] != "[":
                temp_char = List.pop(-1) + temp_char
            List.pop(-1)

            while List[-1].isdigit():
                temp_char_number = List.pop(-1) + temp_char_number

            if temp_char == "":
                List.append(temp_char)
            else:
                number = int(temp_char_number)
                temp_char = number * temp_char
                List.append(temp_char)
            temp_char = ""
            temp_char_number = ""

    temp_char = List.pop(-1)
    while List:
        temp_char = List.pop(-1) + temp_char
    return temp_char

def getCompleteString2(array:str)->str:
    now_string = ""
    pre_now_string_list = []

    quote_string = ""

    number_string = ""
    pre_number = []

    state = 0 # 1,2,3,4 在数字上，在左括号上，在字母上，在右括号上
    last_state = 0

    for ch in array:
        if '[' == ch:
            last_state = state
            state = 2
            pre_now_string_list.append(now_string)
            now_string = ""
            if number_string:
                pre_number.append(int(number_string))
                number_string = ""


        elif ']' == ch:
            last_state = state
            state = 4
            number = pre_number.pop(-1)
            now_string = number * now_string
            print("list = ",pre_now_string_list)
            pre_string = pre_now_string_list.pop(-1)
            now_string = pre_string + now_string
            pre_now_string_list.append(now_string)
            print("now_string = ",now_string , "list = ",pre_now_string_list)

        elif ch.isdigit():
            last_state = state
            state = 1
            number_string = number_string + ch

        elif ch.isalpha():
            last_state = state
            state = 3
            if last_state == 4:
                pre_number.append(1)
            now_string = now_string + ch

    print(pre_now_string_list)
    print(pre_number)
    return now_string

if __name__ == "__main__":
    '''
    保证数字的完结之后一定是'['
    '''
    a = 'ab3[a2[abb]2[cc]5[i]asd]'
    b = 'ab3[a2[ab4[nn2[oo]]b]2[cc]5[i]asd]'
    res = getCompleteString(a)
    res2 = getCompleteString2(a)
    print(res)
    print(res2)