class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i=j
                j+=1
        return len(nums)
    

'''
Algorithm

1. Initialize a write pointer at index 1.
   - This pointer indicates where the next unique element should be placed.

2. Traverse the array from the second element to the last element.

3. For each element:
   - Compare it with the previous element.
   - If the current element is different, it is a unique element.

4. Place the unique element at the write pointer.

5. Increment the write pointer.

6. Continue until all elements have been processed.

7. Return the value of the write pointer, which represents the number of unique elements.

Pattern:
Two Pointers (Read Pointer + Write Pointer)

Time Complexity: O(n)
Space Complexity: O(1)

'''