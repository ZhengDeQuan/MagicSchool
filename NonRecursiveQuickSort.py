'''
非递归的快速排序，
本质就是循环的调用Partitio操作
每次操作后对接下来要进行Partitio的片段，进行入栈
'''

def Partition(List , start  ,end):
    if not start < end:
        return -1
    pivot = List[start]
    i = start + 1
    j = end
    while i < j :
        while j > i and List[j] >= pivot:
            j -= 1
        while i < j and List[i] <= pivot:
            i += 1
        List[i] , List[j] = List[j] , List[i]
    List[i]  , List[start] = List[start] , List[i]
    return i

def QuickSort(List):
    myStack = []
    start = 0
    end = len(List)-1
    myStack.append((start,end))
    while myStack:
        start , end = myStack.pop(-1)
        mid = Partition(List,start,end)
        if mid != -1:
            myStack.append((start,mid-1))
            myStack.append((mid+1,end))


if __name__ == "__main__":
    a = [5,10,3,8,7,6,4,3,2,100]
    QuickSort(a)
    print(a)
