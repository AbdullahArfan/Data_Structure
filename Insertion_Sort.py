def insertion(arr, length):
    for i in range(1, length):
        mainValue = arr[i]
        compareIndex = i-1

        while compareIndex>= 0 and mainValue < arr[compareIndex]:
            arr[compareIndex+1] = arr[compareIndex]
            compareIndex -= 1
        arr[compareIndex+1] = mainValue
        
        print(arr)
        print("-------------------")
    return arr


arr = [6,3,8,1,0,2,7,23,12,65,34]
length = len(arr)
print("Before sorting : ", arr)
print("\n")
print("Every Iteration : ")
print("-------------------")
result = insertion(arr, length)
print("After Sorting : ", result)