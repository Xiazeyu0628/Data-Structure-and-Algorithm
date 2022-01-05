inputList = [3,4,2,6,9,0,1,7,5,8]

class myheap(object):
    def __init__(self,inputList = []):
        self.list = inputList
        self.length = len(self.list)

    def build_heap(self): #迭代创建小根堆
        # 这里//2的考量因素在于遍历所有根茎节点，叶节点因为无法下沉不考虑
        # heapify函数实际上是对传入的arr[i]点在其所有根部节点中确定它的位置；
        # 为什么要逆序，因为要把最底下的小值，一点点bubble上来。
        for node in reversed(range(self.length // 2)): # [4,3,2,1,0]
            self.shift_down(self.list, self.length, node)

    def swift(self,i,j):
        self.list[i],self.list[j] = self.list[j],self.list[i]


    def shift_down(self, arr, length, node):  # 这里参数有n，完全是为了方便写后序的heap_sort
        # k是根节点的index
        # j = 2*k + 1 是左子节点的index
        # j+1 代表的是右子节点的index


        # 没有超过堆的元素的个数的判断用于
        # 完全二叉树存在只有node_left没有node_right的情况
        # 最主要是为了解决堆排序时的堆size逐步缩小的情况


        while 2 * node + 1< length:
            node_left =  2 * node + 1
            waited_swift_node = node_left
            node_right = 2 * node + 2

            if node_right < length:
                if self.list[node_left] > self.list[node_right]:
                    waited_swift_node = node_right

            if self.list[waited_swift_node]<self.list[node]:
                self.swift(waited_swift_node,node)
                node = waited_swift_node
            else:
                break

# 堆排序的核心思想在于，最顶上的根节点一定是最小的值，因为它小于它的子节点，又小于它的孙子节点
# 其他节点尽管因为堆的性质会小于自己的子节点，但是不保证小于同层节点的子节点

    def heap_sort(self):
        n = len(self.list)
        while n>1: # n~[2,n] arr最小的长度为2，即最少有两个节点
            # 当 n = 2 时直接跳出来，你动脑子想一下 [8,9.........] -> [9,8........]
            # 此时shiftDown(arr,1,0)也会直接跳出while循环
            self.swift(0,n-1)
            n = n - 1
            self.shift_down(self.list,n,0)

heap = myheap(inputList)
heap.build_heap()
print(heap.list)
heap.heap_sort()
print(heap.list)




