# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for x in range(len(arr)):
        for y in range(0, len(arr)-x-1):
            if arr[y] > arr[y+1]:
                temp = arr[y+1]
                arr[y+1]=arr[y]
                arr[y]=temp
        


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
