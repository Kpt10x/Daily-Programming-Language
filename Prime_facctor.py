def prime_factorization(N: int) -> list:
    factors = []
    
    while N % 2 == 0:
        factors.append(2)
        N //= 2
        
    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i
            
    if N > 2:
        factors.append(N)
    return factors

# Test cases
print(prime_factorization(18))        
print(prime_factorization(30))        
print(prime_factorization(49))        
print(prime_factorization(19))        
print(prime_factorization(64))        
print(prime_factorization(123456))     
