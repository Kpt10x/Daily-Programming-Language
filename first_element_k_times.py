def kpt10x(arr, k):
    count_map = {}
    for num in arr:
        count_map[num] = count_map.get(num, 0) + 1
    for num in arr:
        if count_map[num] == k:
            return num
    
    
    return -1

arr = [3, 1, 4, 4, 5, 2, 6, 1, 4]
k = 2
print(kpt10x(arr, k))  

arr = [2, 3, 4, 2, 2, 5, 5]
k = 2
print(kpt10x(arr, k))  


arr = [1, 1, 1, 1]
k = 1
print(kpt10x(arr, k)) 


arr = [10]
k = 1
print(kpt10x(arr, k))  

arr = [6, 6, 6, 6, 7, 7, 8, 8, 8]
k = 3
print(kpt10x(arr, k))  

arr = [2, 3, 4, 5]
k = 3
print(kpt10x(arr, k))  
