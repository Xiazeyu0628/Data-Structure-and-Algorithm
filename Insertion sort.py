inputList = [3,4,2,6,9,0,1,7,5,8]


def insertion_sort(inputList):
    for i in range(len(inputList)):
        curValue = inputList[i]
        for j in range(i-1, -1, -1):
            if inputList[j] > curValue:
                inputList[j+1], inputList[j] = inputList[j], inputList[j+1]
            else:
                break

insertion_sort(inputList)
print(inputList)