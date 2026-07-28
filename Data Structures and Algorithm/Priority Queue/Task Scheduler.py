from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how many times each task appears.
        freq = Counter(tasks)
        # Find the highest task frequency.
        max_freq = max(freq.values())
        # Convert frequencies into a list.
        frequencies = list(freq.values())
        # Count how many tasks have the maximum frequency.
        max_freq_task_count = 0
        for count in frequencies:
            if count == max_freq:
                max_freq_task_count += 1
        # Create slots using the most frequent tasks.
        intervals = (max_freq - 1) * (n + 1) + max_freq_task_count

        # If enough different tasks exist, no idle time is needed.
        return max(intervals, len(tasks))

'''
Algorithm

1. Count the frequency of every task.
2. Find max_freq:
   - The highest frequency among all tasks.
3. Count max_freq_task_count:
   - Number of tasks having max_freq frequency.
4. Use the formula:
   intervals =
   (max_freq - 1) × (n + 1)
   + max_freq_task_count
5. Compare intervals with the total number of tasks.
6. Return the larger value.

Pattern:
Greedy + Frequency Counting

Time Complexity:
O(m)

Space Complexity:
O(1)

Where m is the number of tasks.
Since there are only 26 uppercase letters,
the extra space is constant.

'''