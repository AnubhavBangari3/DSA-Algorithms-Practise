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

# Sliding Window

## 3. Longest Substring Without Repeating Characters

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Store characters in current window
        seen = set()

        left = 0
        max_length = 0

        # Expand window using right pointer
        for right in range(len(s)):

            # Remove characters until duplicate is gone
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character
            seen.add(s[right])

            # Calculate current window length
            max_length = max(max_length, right - left + 1)

        return max_length
```

---

## 643. Maximum Average Subarray I

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Sum of first window
        window_sum = sum(nums[:k])

        max_sum = window_sum

        # Slide the window
        for right in range(k, len(nums)):

            # Add new element and remove old element
            window_sum += nums[right]
            window_sum -= nums[right - k]

            # Update maximum sum
            max_sum = max(max_sum, window_sum)

        # Average of best window
        return max_sum / k
```

---

## 567. Permutation in String

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is bigger, permutation is impossible
        if len(s1) > len(s2):
            return False

        # Frequency of characters
        need = {}
        window = {}

        # Count characters of s1
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        left = 0

        for right in range(len(s2)):

            # Add current character to window
            ch = s2[right]
            window[ch] = window.get(ch, 0) + 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                old = s2[left]
                window[old] -= 1

                # Remove zero-count characters
                if window[old] == 0:
                    del window[old]

                left += 1

            # Same frequency means permutation found
            if window == need:
                return True

        return False
```

---

## 424. Longest Repeating Character Replacement

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Store character frequencies
        freq = {}

        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):

            # Add current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Highest frequency inside window
            max_freq = max(max_freq, freq[s[right]])

            # Characters to replace =
            # window size - most frequent character count
            while (right - left + 1) - max_freq > k:

                freq[s[left]] -= 1
                left += 1

            # Update longest valid window
            max_length = max(max_length, right - left + 1)

        return max_length
```

---

# Binary Search

## 704. Binary Search

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            # Find middle
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search right half
            elif nums[mid] < target:
                left = mid + 1

            # Search left half
            else:
                right = mid - 1

        return -1
```

---

## 35. Search Insert Position

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search right
            elif nums[mid] < target:
                left = mid + 1

            # Search left
            else:
                right = mid - 1

        # Left gives correct insertion position
        return left
```

---

## 69. Sqrt(x)

```python
class Solution:
    def mySqrt(self, x: int) -> int:

        # Handle small numbers
        if x < 2:
            return x

        left = 1
        right = x

        while left <= right:

            mid = (left + right) // 2

            square = mid * mid

            # Exact square root
            if square == x:
                return mid

            # Need bigger number
            elif square < x:
                left = mid + 1

            # Need smaller number
            else:
                right = mid - 1

        # right is the floor square root
        return right
```

---

## 33. Search in Rotated Sorted Array

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target lies inside left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                # Target lies inside right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

---

## 153. Find Minimum in Rotated Sorted Array

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            # Minimum is on right side
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum is at mid or on left side
            else:
                right = mid

        return nums[left]
```