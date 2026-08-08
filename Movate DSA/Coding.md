# Strings

## 125. Valid Palindrome

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Keep only letters and numbers and convert to lowercase
        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        # Compare string with its reverse
        return clean == clean[::-1]
```

---

## 242. Valid Anagram

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Different lengths cannot be anagrams
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        # Count characters in s
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        # Count characters in t
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        # Frequencies must match
        return count_s == count_t
```

---

## 344. Reverse String

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:

        # Two pointers
        left = 0
        right = len(s) - 1

        # Swap characters from both ends
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
```

---

## 14. Longest Common Prefix

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Start with first string as prefix
        prefix = strs[0]

        # Compare prefix with every string
        for word in strs[1:]:

            # Reduce prefix until it matches
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                # No common prefix
                if prefix == "":
                    return ""

        return prefix
```

---

## 28. Find the Index of the First Occurrence in a String

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Check every possible starting position
        for i in range(len(haystack) - len(needle) + 1):

            # Compare substring with needle
            if haystack[i:i + len(needle)] == needle:
                return i

        # Not found
        return -1
```

---

## 387. First Unique Character in a String

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Count frequency of each character
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Find first character with frequency 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1
```

---

# Two Pointers

## 125. Valid Palindrome

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Left and right pointers
        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

---

## 167. Two Sum II - Input Array Is Sorted

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Two pointers
        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            # Target found
            if current_sum == target:
                return [left + 1, right + 1]

            # Need a bigger sum
            elif current_sum < target:
                left += 1

            # Need a smaller sum
            else:
                right -= 1
```

---

## 283. Move Zeroes

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        # Position where next non-zero should go
        left = 0

        # Traverse the array
        for right in range(len(nums)):

            # If non-zero is found
            if nums[right] != 0:

                # Swap with left position
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
```

---

## 11. Container With Most Water

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:

            # Width between two lines
            width = right - left

            # Height is limited by shorter line
            current_height = min(height[left], height[right])

            # Calculate area
            area = width * current_height

            # Update maximum area
            max_area = max(max_area, area)

            # Move the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

## 15. 3Sum

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort the array first
        nums.sort()

        result = []

        for i in range(len(nums) - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Found triplet
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Need bigger sum
                elif total < 0:
                    left += 1

                # Need smaller sum
                else:
                    right -= 1

        return result
```