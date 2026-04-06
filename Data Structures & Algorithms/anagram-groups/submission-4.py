class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        
        for string in strs:
            current_chars = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                current_chars[index] += 1

            anagrams_map[tuple(current_chars)].append(string)


        return list(anagrams_map.values())




                