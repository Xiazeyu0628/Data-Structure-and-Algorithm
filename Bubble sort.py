inputList = [3,4,2,6,9,0,1,7,5,8] #从小到大
shortList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#bubble sort是 每一次遍历把当前遍历范围内的最大值搬到最后一位

def bubble_sort(inputList):
    for i in range(len(inputList)-1, 0, -1): #外层控制遍历范围
        for j in range(0, i):
            if inputList[j] > inputList[j+1]:
                inputList[j], inputList[j+1] = inputList[j+1], inputList[j]

def short_bubble_sort(inputList):
    for i in range(len(inputList)-1, 0, -1): #外层控制遍历范围
        flag = True
        for j in range(0, i):
            if inputList[j] > inputList[j+1]:
                inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
                flag = False
        if flag:
            break

#bubble_sort(inputList)

short_bubble_sort(shortList)
print(shortList)






