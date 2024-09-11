def kpt10x(arr):
    
    dheerey = arr[0]
    jaldi = arr[0]
    
   
    while True:
        dheerey = arr[dheerey]
        jaldi = arr[arr[jaldi]]
        if dheerey == jaldi:
            break
    
    
    dheerey = arr[0]
    while dheerey != jaldi:
        dheerey = arr[dheerey]
        jaldi = arr[jaldi]
    
    return dheerey


print(kpt10x([1, 3, 4, 2, 2]))  
print(kpt10x([3, 1, 3, 4, 2]))  
print(kpt10x([1, 1]))           
print(kpt10x([1, 4, 4, 2, 3]))  
print(kpt10x([i for i in range(1, 100000)] + [50000])) 
