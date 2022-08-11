def selection(arr):
    length = len(arr)
    for i in range(0, length-1):
        min = i 
        for j in range(i+1, length):
            if arr[min]>arr[j]:
                min = j
        if  min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr


arr = [6,3,8,1,0,2,7,23,12,65,34]
print("Before sorting : ", arr)
result = selection(arr)
print("After Sorting : ", result)