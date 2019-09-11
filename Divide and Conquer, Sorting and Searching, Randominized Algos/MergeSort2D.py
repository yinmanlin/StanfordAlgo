import sys

def MergeSort2D(num, sortDimension):
    '''
    num is the list of 2D points to be sorted
    sortDimension: 0 means sort by the first dimension, 1 means sort by the second dimension
    '''
    # conquer
    if len(num) == 1:
        return num
    else:
        # divide
        split = int(len(num) / 2)
        list1 = MergeSort2D(num[:split], sortDimension)
        list2 = MergeSort2D(num[split:], sortDimension)
        finalList = []
        i = 0
        j = 0
        # merge the subproblem solution
        while i < len(list1) and j < len(list2):
            if list1[i][sortDimension] < list2[j][sortDimension]:
                finalList.append(list1[i])
                i += 1
            else:
                finalList.append(list2[j])
                j += 1
        # check whether there are any numbers left unjoined
        if (i == len(list1)):
            finalList = finalList + list2[j:]
        else:
            finalList = finalList + list1[i:]
        return finalList

'''         
if __name__ == '__main__':
    inputArray = [int(a) for a in sys.argv[1:]]
    print(inputArray)
    MergeSort(inputArray)


'''
print(MergeSort2D([[1,2],[3,4],[5,0]], 0))
