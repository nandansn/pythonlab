def sortNums(arr):
    

    for i in range(0, len(arr)):
        for k in range(0, len(arr)):
            if arr[k] > arr[i]:
                temp = arr[k];
                arr[k] = arr[i]
                arr[i] = temp

    return arr

arr = [5,3,7,1]
arr = sortNums(arr)

for item  in arr:
    print(item)

        