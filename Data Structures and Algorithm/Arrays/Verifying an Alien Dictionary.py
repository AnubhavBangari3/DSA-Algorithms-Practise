class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={c:i for i,c in enumerate(order)}
        for a,b in zip(words,words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1,s2 in zip(a,b):
                if d[s1] < d[s2]:
                    break
                elif d[s1] > d [s2]:
                    return False
        return True
    
'''
Algorithm

1. Create a hash map to store the rank of every character according to the alien order.
   Example:
   order = "hlabcdefg..."
   h -> 0
   l -> 1
   a -> 2
   b -> 3

2. Compare every adjacent pair of words.
   Example:
   words[i] and words[i + 1]

3. For each pair, compare characters from left to right.

4. If the first different character in word1 has a smaller alien rank than word2,
   then this pair is correctly sorted.
   Move to the next pair.

5. If the first different character in word1 has a greater alien rank than word2,
   then the words are not sorted.
   Return False.

6. If all compared characters are the same, then check length.
   If word1 is longer than word2, then it is invalid.
   Example:
   "apple" before "app" is wrong.
   Return False.

7. If all adjacent word pairs are valid, return True.

Pattern:
Hash Map + Lexicographical Comparison

Time Complexity: O(total characters in words)
Space Complexity: O(1)

'''