
def MergeSortCountInversion(num):
    '''
    num is the list of numbers to be sorted
    '''
    # conquer
    if len(num) == 1:
        return (num, 0)
    else:
        # divide
        split = int(len(num) / 2)
        sortedListLeft, inversionCountLeft = MergeSortCountInversion(num[:split])
        sortedListRight, inversionCountRight = MergeSortCountInversion(num[split:])
        finalList = []
        i = 0
        j = 0
        inversionCountSplit = 0
        # merge the subproblem solution
        while i < len(sortedListLeft) and j < len(sortedListRight):
            if sortedListLeft[i] < sortedListRight[j]:
                finalList.append(sortedListLeft[i])
                i += 1
            else:
                finalList.append(sortedListRight[j])
                j += 1
                inversionCountSplit += (len(sortedListLeft) - i)
        # check whether there are any numbers left unjoined
        if (i == len(sortedListLeft)):
            finalList = finalList + sortedListRight[j:]
        else:
            finalList = finalList + sortedListLeft[i:]
        totalInversionCount = inversionCountLeft + inversionCountRight + inversionCountSplit
        return (finalList, totalInversionCount)

'''         
if __name__ == '__main__':
    inputArray = [int(a) for a in sys.argv[1:]]
    print(inputArray)
    MergeSort(inputArray)


'''

with open('intArray.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content] 
print(len(content))
_, inversionCount = MergeSortCountInversion(content)
print(inversionCount)
