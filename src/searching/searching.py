def linear_search(arr, target):
    # Your code here
    for x in range(len(arr)):
        if arr[x] is target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    list_start = 0
    list_end = len(arr) - 1
    list_middle = 0

    while(list_start <= list_end):
        #reset middle
        list_middle = (list_end + list_start) // 2

        if(arr[list_middle] < target):
            list_start = list_middle + 1

        elif(arr[list_middle] > target):
            list_end = list_middle - 1

        elif(arr[list_middle] == target):
            return list_middle

    return -1  # not found
