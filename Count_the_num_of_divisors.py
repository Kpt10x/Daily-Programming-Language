def kpt10x(N: int) -> int:
    count = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:  
            count += 1  
            if i != N // i:  
                count += 1  
    return count

# Test cases
print(kpt10x(12))   
print(kpt10x(18))   
print(kpt10x(29))  
print(kpt10x(100)) 
print(kpt10x(1))    
print(kpt10x(997))   
