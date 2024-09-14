def kpt10x(arr):
    prefix_sum_map = {}
    result = []
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == 0:
            result.append((0, i))

        if current_sum in prefix_sum_map:
            for start_index in prefix_sum_map[current_sum]:
                result.append((start_index + 1, i))

        if current_sum in prefix_sum_map:
            prefix_sum_map[current_sum].append(i)
        else:
            prefix_sum_map[current_sum] = [i]

    return result


# Test Cases:

arr1 = [-3, 1, 2, -3, 4, 0]
print("Subarrays with zero sum:", kpt10x(arr1))  

arr2 = [1, -1, 2, -2, 3, -3] * 10000
result = kpt10x(arr2)
print("Number of subarrays with zero sum:", len(result))  

arr3 = [0]
print("Subarrays with zero sum:", kpt10x(arr3))  

arr4 = [0, 0, 0]
print("Subarrays with zero sum:", kpt10x(arr4))  
