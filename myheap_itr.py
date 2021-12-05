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
    while 2 * k + 1 < n: # 没有超过堆的元素的个数
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] < arr[j]:  # 如果右子节点小于左子节点
            j += 1  #那么即将下降交换的是右子节点

        if arr[k] <= arr[j]:  #根节点小于最小的子节点
            break # 不交换
        else: #根节点大于最小的子节点
            arr[k], arr[j] = arr[j], arr[k] # 交换
            k = j #当前根节点来到交换之后的下标，继续判断是否还需要下沉

heapify(inputList)
print(inputList)

# 堆排序的核心思想在于，最顶上的根节点一定是最小的值，因为它小于它的子节点，又小于它的孙子节点
# 其他节点尽管因为堆的性质会小于自己的子节点，但是不保证小于同层节点的子节点

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

