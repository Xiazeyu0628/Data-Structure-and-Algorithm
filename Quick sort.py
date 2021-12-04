# 分而治之

inputList = [3,4,2,6,9,0,1,7,5,8]

def quick_sort(inputList): #参数与返回值

    #中止条件
    if not inputList:
        return []

    #单层逻辑
    partition = inputList[len(inputList)//2]
    leftpart = quick_sort([ele for ele in inputList if ele<partition])
    rightpart = quick_sort([ele for ele in inputList if ele>partition])

    return leftpart+[partition]+rightpart

result = quick_sort(inputList)
print(result)