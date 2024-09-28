def kpt10x(s: str) -> list:
    def backtrack(path, used):
        if len(path) == len(s):
            result.append(''.join(path))
            return
        for i in range(len(s)):
            if used[i]:
                continue
    
            if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(s[i])
            backtrack(path, used)
            used[i] = False
            path.pop()

    result = []
    s = sorted(s)  
    used = [False] * len(s)
    backtrack([], used)
    return result

# Test cases
print(kpt10x("abc")) 
print(kpt10x("aab"))  
print(kpt10x("aaa")) 
print(kpt10x("a"))    
print(kpt10x("abcd"))  
