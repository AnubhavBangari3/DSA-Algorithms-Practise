class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        d={}
        longest=0
        for num in nums:
            x=d.get(num-1,0)
            y=d.get(num+1,0)

            c=x+y+1
            d[num-x]=c
            d[num+y]=c
            longest=max(longest,c)
        return longest
    
'''
Algorithm

1. Remove duplicate elements by converting the array into a set.
2. Create a hash map to store the length of consecutive sequences at their boundaries.
3. Traverse each unique number.
4. For the current number:
   - Find the length of the consecutive sequence ending at num - 1.
   - Find the length of the consecutive sequence starting at num + 1.
5. Merge the left and right sequences with the current number.
6. Update the total length of the merged sequence at both boundaries.
7. Keep track of the maximum sequence length found.
8. Return the maximum length.

Pattern:
Hash Map + Boundary Merging

Time Complexity: O(n)
Space Complexity: O(n)

'''