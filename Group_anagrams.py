from collections import defaultdict
def kpt10x(strs: list) -> list:
    anagrams = defaultdict(list)
    for s in strs:
        sorted_s = ''.join(sorted(s))
        
        anagrams[sorted_s].append(s)
    

    return list(anagrams.values())


print(kpt10x(["eat", "tea", "tan", "ate", "nat", "bat"]))  
print(kpt10x([""]))  
print(kpt10x(["a"]))  
print(kpt10x(["abc", "bca", "cab", "xyz", "zyx", "yxz"]))  
print(kpt10x(["abc", "def", "ghi"]))  
