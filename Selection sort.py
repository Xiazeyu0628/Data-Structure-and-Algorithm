inputList = [3,4,2,6,9,0,1,7,5,8] #从小到大

#选择是 每一次遍历把当前遍历范围内的最小值搬到最前面一位，他和冒泡排序的风格是正好相反的

def selection_sort(inputList):
    for i in range(len(inputList)): #外层控制遍历范围
        for j in range(i+1,len(inputList)):
            if inputList[j]<inputList[i]:
                inputList[i], inputList[j] = inputList[j], inputList[i]


def index_selection_sort(inputList):
    for i in range(len(inputList)): #外层控制遍历范围
        minIndex = i
        for j in range(i+1,len(inputList)):
            if inputList[j]<inputList[minIndex]:
                minIndex = j
        inputList[i], inputList[minIndex] = inputList[minIndex], inputList[i]

index_selection_sort(inputList)
print(inputList)




