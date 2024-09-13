def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)
    
    return leaders[::-1]

# Test cases
print(find_leaders([16, 17, 4, 3, 5, 2]))  
print(find_leaders([1, 2, 3, 4, 0]))      
print(find_leaders([7, 10, 4, 10, 6, 5, 2]))  
print(find_leaders([5]))                   
print(find_leaders([100, 50, 20, 10]))     
