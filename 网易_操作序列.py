

if __name__ == "__main__":
    n = int(input())
    numbers = list( map(int, input().split()) )
    new_numbers = [0] * n
    if n%2 == 0:
        half = n/2
        i = 0
        while i < half:
            new_numbers[i] = numbers[n-1-2*i]
            i += 1
        j = 0
        while j < half:
            new_numbers[i+j] = numbers[j * 2]
            j += 1
        print(new_numbers)
    else:
        mid_idex = int(n/2)
        i = 0
        while i <= mid_idex:
            new_numbers[i] = numbers[n-1-2*i]
            i += 1
        j = 1
        for iter in range(mid_idex):
            # print("iter = ",iter)
            new_numbers[i+int(j/2)] = numbers[j]
            j += 2
        print(new_numbers)

