
def inRa(arr):
    for i in arr:
        print(i,end=' ')
    print()



arr = [1, 2, 3, 4, 5]
arr.sort()
arr_2 = arr.copy()
arr_2.sort(reverse=True)
while arr!=arr_2:
    for i in range(len(arr)-2,-1,-1):
        if(arr[i]<arr[i+1]):
            for j in range(len(arr)-1,i,-1):
                if(arr[j]>arr[i]):
                    arr[i],arr[j] = arr[j],arr[i]
                    break
            arr = arr[:i+1] + sorted(arr[i+1:])
            inRa(arr)
            break

