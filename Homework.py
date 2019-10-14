#Question number 5
import random 
array1 = [random.randint(1,10) for _ in range(10000)]

array2 = (range(1,10000))

array3 = (range(10000,1))

arry = [10,9,8,7,6,5,4,3,2,1]
#bubble sort 
def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

#selection sort
def selectionSort(arr):
    for i in range(len(arr)): 
        
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
                    
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
#shell sort
def shellSort(arr):
     gap = len(arr) // 2
     while gap > 0:
         for i in range(gap, len(arr)):
             val = arr[i]
             j = i
             while j >= gap and arr[j - gap] > val:
                 arr[j] = arr[j - gap]
                 j -= gap
             arr[j] = val
         gap //= 2

#merge sort
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

#quick sort
def quicksort_recursive(arr):
    if len(arr) == 0:
        return arr
    p = len(arr) // 2
    l = [i for i in arr if i < a[p]]
    m = [i for i in arr if i == a[p]]
    r = [i for i in arr if i > a[p]]
    return quicksort_recursive(l) + m + quicksort_recursive(r)

#insertion sort
def insertionSort(arr): 

    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1

        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
