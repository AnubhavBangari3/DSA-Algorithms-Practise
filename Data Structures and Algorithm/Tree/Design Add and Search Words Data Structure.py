class WordDictionary:

    def __init__(self):
        # Each node stores 26 children (a-z)
        self.children = [None] * 26

        # Marks whether a complete word ends at this node
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        # Start from the root
        curr = self

        # Insert each character into the Trie
        for c in word:
            index = ord(c) - ord('a')

            # Create a new node if it doesn't exist
            if curr.children[index] is None:
                curr.children[index] = WordDictionary()

            # Move to the next node
            curr = curr.children[index]

        # Mark the end of the word
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        # Start from the current node (root initially)
        curr = self

        # Traverse every character in the search word
        for i in range(len(word)):
            c = word[i]

            # Wildcard '.' can match any character
            if c == '.':
                # Try all possible child nodes
                for child in curr.children:
                    if child is not None and child.search(word[i + 1:]):
                        return True
                return False

            index = ord(c) - ord('a')

            # Character not found
            if curr.children[index] is None:
                return False

            # Move to the next node
            curr = curr.children[index]

        # Word exists only if current node marks end of a word
        return curr is not None and curr.isEndOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

'''

Algorithm (Trie + DFS for Wildcard Search)

1. Create a Trie node containing:
   - children → array of 26 child pointers (one for each lowercase letter).
   - isEndOfWord → indicates whether a complete word ends at this node.

2. addWord(word)
   - Start from the root.
   - Traverse each character in the word.
   - If the corresponding child does not exist, create a new Trie node.
   - Move to that child.
   - After processing the last character, mark isEndOfWord = True.

3. search(word)
   - Start from the root.
   - Traverse each character in the word.
   - If the character is a lowercase letter:
       - If its child does not exist, return False.
       - Otherwise, move to that child.
   - If the character is '.':
       - Recursively search all non-null children using the remaining substring.
       - If any recursive call returns True, return True.
       - Otherwise, return False.
   - After processing all characters, return True only if isEndOfWord is True.


   Time Complexity:
• addWord()  : O(L)
• search()   :
    - Without '.'       : O(L)
    - With '.' wildcard : O(26^d × L)
      where d = number of '.' characters (at most 2 in this problem)

Space Complexity:
• addWord()  : O(L) (new nodes in worst case)
• search()   : O(L) recursion stack in worst case
'''