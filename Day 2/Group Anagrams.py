from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_words = defaultdict(list)

        def count(word):
            freq={}

            for char in word:
                freq[char] = freq.get(char,0) + 1

            return tuple(sorted(freq.items()))
        
        for word in strs:
            key = count(word)
            
            freq_words[key].append(word)
        
        return list(freq_words.values())
#

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            freq = [0] * 26

            for char in word:
                freq[ord(char) - ord('a')] += 1

            groups[tuple(freq)].append(word)

        return list(groups.values())