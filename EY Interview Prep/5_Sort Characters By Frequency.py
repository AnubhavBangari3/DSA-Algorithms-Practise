"""
451. Sort Characters By Frequency

Problem:
Given a string s, sort characters in decreasing order
based on frequency.

Characters with higher frequency should appear first.

Return any valid answer.

Examples:

Input: s = "tree"
Output: "eert"

Input: s = "cccaaa"
Output: "aaaccc"

Input: s = "Aabb"
Output: "bbAa"

Constraints:
- 1 <= s.length <= 5 * 10^5
- Contains uppercase, lowercase letters and digits
"""

# -------------------------
# Pattern Used
# -------------------------
"""
Pattern: HashMap + Sorting
"""

# -------------------------
# Algorithm
# -------------------------
"""
1. Create frequency hashmap

2. Count occurrences of each character

3. Sort hashmap items based on frequency
   in descending order

4. Build answer string:
      character * frequency

5. Join all pieces and return
"""

class Solution:
    def frequencySort(self, s):

        frequencyCount = {}

        # Count frequency
        for char in s:
            frequencyCount[char] = frequencyCount.get(char, 0) + 1

        # Sort by frequency descending
        sortedChars = sorted(
            frequencyCount.items(),
            key=lambda item: item[1],
            reverse=True
        )

        result = []

        # Build output string
        for char, count in sortedChars:
            result.append(char * count)

        return "".join(result)


# -------------------------
# Complexity Analysis
# -------------------------
"""
Time Complexity: O(n log k)

Explanation:

Counting frequencies:
O(n)

Sorting unique characters:
O(k log k)

Building final answer:
O(n)

Overall:
O(n + k log k)

where:
n = length of string
k = unique characters
"""

"""
Space Complexity: O(k)

Explanation:

Hashmap stores frequencies
Result list stores unique groups

k = unique characters
"""