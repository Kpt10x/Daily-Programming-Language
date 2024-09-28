def length_of_longest_substring(s: str) -> int:
    char_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
            
        char_map[s[right]] = right
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("bbbbb"))    
print(length_of_longest_substring("pwwkew"))   
print(length_of_longest_substring("abcdefgh")) 
print(length_of_longest_substring("a"))          
