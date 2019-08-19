import sys

def MergeSort(num):
    '''
    num is the list of numbers to be sorted
    '''
    if len(num) == 1:
        return num
    else:
        split = int(len(num) / 2)
        list1 = MergeSort(num[:split])
        list2 = MergeSort(num[split:])
        finalList = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                finalList.append(list1[i])
                i += 1
            else:
                finalList.append(list2[j])
                j += 1
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
print(MergeSort([3,5,7,2,1,9,0]))
