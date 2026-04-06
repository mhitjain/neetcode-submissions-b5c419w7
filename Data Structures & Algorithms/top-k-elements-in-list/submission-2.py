class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [set() for _ in range(len(nums))]

        c = Counter(nums)
        for key,v in c.items():
            bucket[v-1].add(key)

        res = []
        while len(res)!=k:
            cur = bucket.pop()
            for e in cur:
                res.append(e)
        return res
            




        