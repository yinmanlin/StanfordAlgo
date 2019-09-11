import random
def sub_partition(array, start, end, idx_pivot):

    'returns the position where the pivot winds up'

    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    array[start], array[idx_pivot] = array[idx_pivot], array[start]
    pivot = array[start]
    i = start + 1
    j = start + 1

    while j <= end:
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[start], array[i - 1] = array[i - 1], array[start]
    return i - 1

def quicksort(array, start=0, end=None):

    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    idx_pivot = 0 #random.randint(start, end)
    i = sub_partition(array, start, end, idx_pivot)
    #print array, i, idx_pivot
    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)


with open('QuickSort.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [int(x.strip()) for x in content] 
partContent = content[:10]
# print(len(content))
quicksort(partContent, 0, None)
