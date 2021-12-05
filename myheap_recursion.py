inputList = [3,4,2,6,9,0,1,7,5,8]

def heapify(arr): #迭代创建小根堆
    n = len(arr)
    # 这里//2的考量因素在于遍历所有根茎节点，叶节点因为无法下沉不考虑
    # eapify函数实际上是对传入的arr[i]点在其所有根部节点中确定它的位置；
    # 为什么要逆序，因为要把最底下的小值，一点点bubble上来。
    for i in reversed(range(n // 2)): # [4,3,2,1,0]
        shiftDown(arr,n,i)

def shiftDown(arr, n, k):  # 这里参数有n，完全是为了方便写后序的heap_sort
    # k是根节点的index
    # j = 2*k + 1 是左子节点的index
    # j+1 代表的是右子节点的index
    rootnode = k
    leftindex = 2*k + 1
    rightindex = 2*k + 2

    if leftindex < n: # 没有超过堆的元素的个数
        if rightindex < n and arr[rightindex] < arr[leftindex]:  # 如果右子节点小于左子节点
            smallest = rightindex  #那么即将下降交换的是右子节点
        else:
            smallest = leftindex

        if arr[rootnode] > arr[smallest]:  #根节点大于最小的子节点
            arr[rootnode], arr[smallest] = arr[smallest], arr[rootnode] # 交换
            rootnode = smallest #当前根节点来到交换之后的下标，继续判断是否还需要下沉
            shiftDown(arr,n,rootnode)

heapify(inputList)
print(inputList)

def heap_sort(arr):
    n = len(arr)
    while n>1: # n~[2,n] arr最小的长度为2，即最少有两个节点
        # 当 n = 2 时直接跳出来，你动脑子想一下 [8,9.........] -> [9,8........]
        # 此时shiftDown(arr,1,0)也会直接跳出while循环
        inputList[0],inputList[n-1] = inputList[n-1],inputList[0] # n-1代表的是末尾index
        n = n - 1
        shiftDown(arr,n,0)

heap_sort(inputList)
print(inputList)