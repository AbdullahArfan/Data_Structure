def linearSearch(arr, length, value):
    for i in range(0, length):
        if (arr[i] == value):
            return i
    return -1

arr = [5,98,3,45,7,2,9,27,35,56,78,4]

value = int(input("Enter your a value to check :  "))
length = len(arr)

myResult = linearSearch(arr, length, value)

if (myResult == -1):
    print("Element not found")
else:
    print("Element found at index: ", myResult)
    