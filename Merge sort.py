inputList = [3,4,2,6,9,0,1,7,5,8]

def merge_sort(inputList): #

    def merge(leftPart, rightPart):
        result = []
        leftLength = len(leftPart)
        rightLength = len(rightPart)
        L = 0
        R = 0
        while L <= leftLength - 1 and R <= rightLength - 1:
            if leftPart[L] >= rightPart[R]:
                result.append(rightPart[R])
                R = R + 1
            else:
                result.append(leftPart[L])
                L = L + 1

        result = result + leftPart[L:] if L <= leftLength - 1 else result + rightPart[R:]
        return result

    # 递归结束条件
    if len(inputList)<=1:
        return inputList
    else:
        length = len(inputList) 
        divideIndex = (length-1)//2
        leftPart = merge_sort(inputList[:divideIndex+1])
        rightPart = merge_sort(inputList[divideIndex+1:])
        return merge(leftPart,rightPart)


print(merge_sort(inputList))