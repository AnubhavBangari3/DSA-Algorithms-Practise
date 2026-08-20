
class Solution:
    def ladderLength( self, beginWord: str, endWord: str, wordList: List[str] ) -> int:

        # endWord must exist in wordList
        if endWord not in wordList:
            return 0

        # pattern -> list of matching words
        neighbors = defaultdict(list)

        # Include beginWord while building patterns
        wordList.append(beginWord)

        # Build pattern mapping
        for word in wordList:
            for i in range(len(word)):

                pattern = word[:i] + "*" + word[i + 1:]

                neighbors[pattern].append(word)

        # BFS queue
        queue = deque([beginWord])

        # Visited words
        visited = {beginWord}

        # beginWord counts as first word
        length = 1

        # BFS level by level
        while queue:

            for _ in range(len(queue)):

                word = queue.popleft()

                # Target reached
                if word == endWord:
                    return length

                # Generate all patterns
                for i in range(len(word)):

                    pattern = word[:i] + "*" + word[i + 1:]

                    # Visit neighboring words
                    for neighbor in neighbors[pattern]:

                        if neighbor not in visited:

                            visited.add(neighbor)
                            queue.append(neighbor)

            # Move to next transformation level
            length += 1

        return 0
'''
1. If `endWord` is not in `wordList`, return `0`.
2. Build a pattern map for every word.
3. For each character position, replace that character with `*`.

Example:

`hot → *ot, h*t, ho*`

4. Words having the same pattern are neighbors because they differ by one character.
5. Use **BFS** starting from `beginWord`.
6. BFS is used because we need the **shortest transformation sequence**.
7. For every word:
   - Generate all its patterns.
   - Visit all words connected to those patterns.
8. If `endWord` is reached, return the current level.
9. If BFS finishes without finding it, return `0`.

Complexity

Let N = number of words and L = length of each word.

Time Complexity: O(N × L²)
Space Complexity: O(N × L)
'''