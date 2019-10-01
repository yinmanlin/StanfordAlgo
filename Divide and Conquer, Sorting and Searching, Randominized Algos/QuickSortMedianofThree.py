
def Partition(numList, start, end, pivotPosition, totalComparison):
    i = start
    j = i + 1
    pivot = numList[pivotPosition]
    # exchange the pivot with the first element
    numList[start], numList[pivotPosition] = numList[pivotPosition], numList[start]
    if end - start <= 0:
        return (i, totalComparison)
    else:
        totalComparison += end - start
        while j <= end:
            if numList[j] >= pivot:
                j += 1
            elif numList[j] < pivot:
                numList[i+1], numList[j] = numList[j], numList[i+1]
                i += 1
                j += 1
        numList[start] = numList[i]
        numList[i] = pivot
    return (i, totalComparison)


def QuickSortCountComparisons(numList, totalComparison, start, end):
    '''
    This algorithm sorts in place, so no need to return a sorted list
    '''

    if end - start < 1:
        return totalComparison
    
    a = numList[start]
    b = numList[end]
    c = numList[(int)((start+end)/2)]

    if (a >= b and b >= c) or (c >= b and b >= a):
        pivotPosition = end
    elif (b >= c and c >= a) or (a >= c and c >= b):
        pivotPosition = (int)((start+end)/2)
    elif (b >= a and a >= c) or (c >= a and a >= b):
        pivotPosition = start
   
    split, totalComparison = Partition(numList, start, end, pivotPosition, totalComparison)
    totalComparison  = QuickSortCountComparisons(numList, totalComparison, start, split - 1)
    totalComparison  = QuickSortCountComparisons(numList, totalComparison, split + 1, end)

    return totalComparison


with open('QuickSort.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content] 
partContent = content[:10]
print(len(content))
comparisonCount = QuickSortCountComparisons(content, 0, 0, len(content)-1)
print(comparisonCount)









