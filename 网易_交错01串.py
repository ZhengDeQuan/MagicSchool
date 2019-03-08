

if __name__ == "__main__":
    s_numbers = input()
    length = len(s_numbers)
    start_index = 0
    max_len = 0
    last_ch = "a"
    cur_ch = ""
    cur_len = 0
    for i in range(length):
        cur_ch = s_numbers[i]
        if last_ch!=cur_ch:
            cur_len += 1
            max_len = max(max_len,cur_len)
        else:
            cur_len = 1
            max_len = max(max_len,cur_len)
        last_ch = cur_ch
    print(max_len)
