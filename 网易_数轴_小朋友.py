

if __name__ == "__main__":
    n,s = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    mid_num = (max_num - min_num)/2 + min_num

    if numbers[0] >= mid_num:
        min_num = numbers[0] - s
        max_num = numbers[0] - s
    else:
        min_num = numbers[0] + s
        max_num = numbers[0] + s
    for num in numbers[1:]:
        new_num = num - s if num >= mid_num else num + s
        if new_num > max_num:
            max_num = new_num
        if new_num < min_num:
            min_num = new_num
    print(max_num - min_num)


