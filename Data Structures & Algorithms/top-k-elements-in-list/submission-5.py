class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
         # Step 1 — count frequencies
        count = Counter(nums)

        # Step 2 — buckets indexed by frequency
        # index i = numbers that appear i times
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        # Step 3 — collect from highest frequency down
        result = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
            




        