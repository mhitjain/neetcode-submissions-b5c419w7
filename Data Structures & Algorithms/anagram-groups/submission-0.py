class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = []  
        res = []
        for i in range(len(strs)):
            s = strs[i]
            found= False
            c = Counter(s)
            for i in range(len(hashmap)):
                if hashmap[i]==c:
                    res[i].append(s)
                    found=True
                    break
            if not found:
                res.append([s])
                hashmap.append(c)
            
        return res
        