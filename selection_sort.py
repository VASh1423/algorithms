def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr [i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    while arr:
        newArr.append(arr.pop(findSmallest(arr)))
    return newArr

print(selectionSort([5, 3, 8, 1, 4, 0. -1, 0, 5, 10]))