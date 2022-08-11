def binarySearch(arr, small, big, value):
    if big >= small:
        mid = (small + big)//2
        if arr[mid] == value:
            return mid
        elif arr[mid]<value:
            return binarySearch(arr, mid+1, big, value)
        else:
            return binarySearch(arr, small, mid-1, value)
    else:
        return -1
    
myArray = [2,4,6,8,13,17,19,22,27,376,49,58,66,72]

value = int(input("Enter a value to check : "))

arraylength = len(myArray)

result = binarySearch(myArray, 0, arraylength-1, value)

if result != -1:
    print("Value found at index : ", result)
else:
    print("Value not found! ")