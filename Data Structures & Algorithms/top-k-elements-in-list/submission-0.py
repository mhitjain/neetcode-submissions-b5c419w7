class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = Counter(nums)
        res = []
        for i in range(k):
            max_key = max(h, key=h.get)
            res.append(max_key)
            del h[max_key]
        return res


        