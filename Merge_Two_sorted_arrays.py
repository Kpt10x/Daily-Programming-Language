import math

def next_gap(gap):
    if gap <= 1:
        return 0
    return math.ceil(gap / 2)

def merge(arr1, arr2, m, n):
    gap = next_gap(m + n)
    
    while gap > 0:
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1
        
       
        j = max(0, gap - m)  
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1
        
       
        if j < n:
            k = 0
            while j + k < n:
                if arr2[j] > arr2[j + k]:
                    arr2[j], arr2[j + k] = arr2[j + k], arr2[j]
                k += 1
        
      
        gap = next_gap(gap)


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merge(arr1, arr2, len(arr1), len(arr2))
print(arr1) 
print(arr2) 

arr1 = [10, 12, 14]
arr2 = [1, 3, 5]
merge(arr1, arr2, len(arr1), len(arr2))
print(arr1)  
print(arr2) 

arr1 = [2, 3, 8]
arr2 = [4, 6, 10]
merge(arr1, arr2, len(arr1), len(arr2))
print(arr1)  
print(arr2)  

arr1 = [1]
arr2 = [2]
merge(arr1, arr2, len(arr1), len(arr2))
print(arr1)  
print(arr2)  
