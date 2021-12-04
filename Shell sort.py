inputList = [3,4,2,6,9,0,1,7,5,8]

def shell_sort(inputList):

    def insertion_sort(startIndex, gap):
        subList_length = ((len(inputList) - 1 - startIndex) // gap) + 1 #当前要处理的子列表的长度
        for multiple in range(subList_length):
            m = startIndex + gap * multiple
            curValue = inputList[m]
            nstart = startIndex + gap * (multiple-1)
            for n in range(nstart, -1, -1 * gap):
                if inputList[n] > curValue:
                    inputList[n + gap], inputList[n] = inputList[n], inputList[n + gap]
                else:
                    break

    gapList = []
    Length = len(inputList)/2 # 除2是因为，如果数组长为10，间隔为9，这样的大间隔没有意义

    k = 1
    # 间隔k   n = 2k-1
    while 2*k-1<Length: # 间隔不能等于数组长度，否则必然越界
        gapList.append(2*k-1)
        k = k+1

    for i in range(len(gapList)-1,-1,-1):
        gapValue = gapList[i]  #3
        for j in range(gapValue): #startIndex
            insertion_sort(j,gapValue)



shell_sort(inputList)
print(inputList)


