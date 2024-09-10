def kpt10x(arr):
    n = len(arr) + 1  
    tot_sum = n * (n + 1) // 2 
    arr_sum = sum(arr)  
    missing_number = tot_sum - arr_sum 
    return missing_number


print(kpt10x([1, 2, 4, 5])) 
print(kpt10x([2, 3, 4, 5]))  
print(kpt10x([1, 2, 3, 4])) 
print(kpt10x([1]))          
print(kpt10x(list(range(1, 1000000))))  
