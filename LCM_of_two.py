import math
def kpt10x(N: int, M: int) -> int:
    gcd_value = math.gcd(N, M)
    kpt10x_value = (N * M) // gcd_value
    return kpt10x_value
print(kpt10x(4, 6))          
print(kpt10x(5, 10))         
print(kpt10x(7, 3))           
print(kpt10x(1, 987654321))   
print(kpt10x(123456, 789012))
