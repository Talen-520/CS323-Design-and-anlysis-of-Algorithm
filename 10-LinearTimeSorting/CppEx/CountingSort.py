arr = [1,0,3,1,3,1]

def countingSort(arr):
    max_val = max(arr)
    min_val = min(arr)
    
    count = [0]*(max_val-min_val + 1) #counting arr in range max - min
    
    for num in arr:
        count[num - min_val] +=1

    #after loop we get [1,3,0,2]
    
    #when i = 0, count[i] = 1
    #arr[0] = 0 + 0
    #when i = 1 count[1] = 3
    #arr[1] = 1 + 0 = 1
    #arr[2] = 1 + 0 = 1
    #arr[3] = 1 + 0 = 1
    #prefixSum = 4
    index=0
    for i in range(len(count)):
        for _ in range(count[i]):
            arr[index] = i + min_val
            index+=1
    return arr

print(countingSort(arr))