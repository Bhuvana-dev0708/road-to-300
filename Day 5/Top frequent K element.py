class Solution:
    def topKFrequent(nums, k):



    freq = {}

    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

        
    sorted_nums = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    
    result = []
    for num, count in sorted_nums[:k]:
        result.append(num)

    return result