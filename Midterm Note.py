arr = [1,4,7,3,2]
def partition2(arr, left, right):
    if left>=right:
        return left
    pivot,i,j = arr[left],left+1,right
    #move element < pivot to left side, > pivot to right side by swap
    while True:
        while arr[i] < pivot and i < j: i+=1
        while arr[j] > pivot: j-=1
        if i >= j:
            break
        arr[i],arr[j] =arr[j],arr[i]
        i+=1
        j-=1
    #swap pivot with position of j 
    arr[left], arr[j] = arr[j],arr[left]
    return j
def QS (arr,left,right):
    if left>=right:
        return 
    index = partition2(arr,left,right)
    QS(arr,left,index-1)
    QS(arr,index+1,right)
QS(arr,0,len(arr)-1)
print(arr)

#counting sort
arr = [3,5,6,1,1,1,2]
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    count = [0]* (max_val - min_val+1)
    #get number 
    for num in arr:
        count[num-min_val]+=1
    #print(count) #[3, 1, 1, 0, 1, 1] from range 1-6 6element counting
    index = 0
    for i in range(len(count)):
        for _ in range(count[i]):
            arr[index] = i+min_val #occurence 0 skip 
            index +=1
counting_sort(arr)
print(arr)


import heapq

# Create a list (or an array)
my_list = [5, 2, 8, 1]
print(f"my list: {my_list}")
# Convert the list into a max heap
#heapq._heapify_max(my_list)
print(f"my heap: {my_list}")

# Convert the list into a min-heap (priority_queue)
heapq.heapify(my_list)

heapq.heappush(my_list, 5)  # Insert an element with priority 5
print(f"my list after push 5: {my_list}")

highest_priority = heapq.heappop(my_list)

print(f"my list after pop: {my_list}")

highest_priority_element = my_list[0]# top()
print(f"my list after top: {highest_priority_element}")
