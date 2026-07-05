class Solution:
    def romanToInt(self, s: str) -> int:
        res,prev=0,0
        d={
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
        }
        
        for i in s[::-1]:
            if d[i] >= prev:
                res+=d[i] #sum the vals if prev val is same or more
                #print(res)
            else:
                res-=d[i] #subtract the val when is "IV -->5-1"
                #print(res)
            prev=d[i] 
        return res
        
'''
Algorithm

1. Create a hash map to store the integer value of each Roman numeral.
2. Initialize the result as 0 and the previous numeral value as 0.
3. Traverse the Roman numeral string from right to left.
4. For each character:
   - Get its integer value from the hash map.
   - If the current value is greater than or equal to the previous value, add it to the result.
   - Otherwise, subtract it from the result.
5. Update the previous value to the current value.
6. After processing all characters, return the result.

Pattern:
Hash Map + Reverse Traversal


'''