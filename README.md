# Data-Structure-and-Algorithm
## 排序算法
1 冒泡排序
2 选择排序
3 插入排序
4 快速排序
5 希尔排序
6 归并排序


## 堆heap
堆最重要的性质：
大顶堆：每个节点的值都大于或等于其子节点的值，根节点为全局最大值，在堆排序算法中用于升序排列；
小顶堆：每个节点的值都小于或等于其子节点的值，根节点为全局最小值，在堆排序算法中用于降序排列；

###自建堆(build_heap)
**思路**：从列表直接创建堆构建shift_down(node,len)函数，shift_down用于维护以传入的node节点为根节点的heap结构。一方面，我们需要保证每一个节点都下降到不能再下降为止，即最底下的小值不被shift上来最上面的大值就没法完全沉下去，另一方面，每一次shift_down都会可能会破坏上方的堆结构，因此我们需要从后往前遍历节点。由于叶节点没有子节点无需比较，我们只需要从最后一个有子节点的节点反向遍历即可。  

**步骤**:
1. 找到最后一个要遍历的node
2. shift_down
3. 再找上一个node，重复操作直到根节点


**时间复杂度O(n)是怎么来的**
![](../../../../../var/folders/35/0lxq769j30jbkyy97nd62vv40000gn/T/TemporaryItems/（screencaptureui正在存储文稿）/截屏2022-01-05 18.29.24.png)

### 堆排序
1. 将待排序序列构建成一个堆 H[0……n-1]，根据（升序降序需求）选择大顶堆或小顶堆；

2. 把堆首（最大值）和堆尾互换；

3. 把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；

4. 重复步骤 2，直到堆的尺寸为 1。



## Reference
自建堆和堆排序部分:  

https://blog.csdn.net/hrn1216/article/details/51465270
https://www.runoob.com/w3cnote/heap-sort.html
https://blog.csdn.net/Winnie_boy/article/details/117295050  

算法复杂度部分:  

https://www.zhihu.com/question/20729324
https://blog.csdn.net/LeoSha/article/details/46116959?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&utm_relevant_index=1