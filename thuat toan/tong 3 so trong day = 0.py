def countTriplets(A, n):
    A.sort()
    count = 0
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            total = A[i] + A[left] + A[right]
            
            if total == 0:
                count += 1
                left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return count

t = int(input())
for i in range(t):
    n = int(input())
    st = input()
    st = st.split()
    arr = []
    for j in st:
        arr.append(int(j))
    result = countTriplets(arr, n)
    print(result)
