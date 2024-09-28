def kpt10x(s: str) -> str:
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    
    if len(s) < 2:
        return s
    
    longest = ""
    
    for i in range(len(s)):
        odd_palindrome = expand_around_center(s, i, i)
        even_palindrome = expand_around_center(s, i, i + 1)
        
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    
    return longest

# Test cases
print(kpt10x("babad"))  
print(kpt10x("cbbd"))   
print(kpt10x("a"))      
print(kpt10x("aaaa"))   
print(kpt10x("abc"))    
