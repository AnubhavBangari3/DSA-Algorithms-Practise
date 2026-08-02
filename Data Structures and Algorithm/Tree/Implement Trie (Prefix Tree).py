class TrieNode:
    def __init__(self):
        # Stores the next characters.
        self.children = {}

        # True if a complete word ends here.
        self.is_end = False


class Trie:

    def __init__(self):
        # Root node does not store any character.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root.
        node = self.root

        # Process every character.
        for ch in word:

            # Create a new node if the character is not present.
            if ch not in node.children:
                node.children[ch] = TrieNode()

            # Move to the next character.
            node = node.children[ch]

        # Mark the end of the complete word.
        node.is_end = True

    def search(self, word: str) -> bool:
        # Start from the root.
        node = self.root

        # Traverse every character.
        for ch in word:

            # Word does not exist.
            if ch not in node.children:
                return False

            # Move to the next character.
            node = node.children[ch]

        # Return True only if this is the end of a word.
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        # Start from the root.
        node = self.root

        # Traverse every character of the prefix.
        for ch in prefix:

            # Prefix does not exist.
            if ch not in node.children:
                return False

            # Move to the next character.
            node = node.children[ch]

        # All prefix characters were found.
        return True

'''
Algorithm (Trie / Prefix Tree)

1. Create a root node containing:
   - children → stores the next characters.
   - is_end → indicates whether a complete word ends at this node.

2. Insert(word)
   - Start from the root.
   - Traverse each character in the word.
   - If the character does not exist in children, create a new Trie node.
   - Move to the corresponding child node.
   - After processing the last character, mark is_end = True.

3. Search(word)
   - Start from the root.
   - Traverse each character in the word.
   - If any character is missing, return False.
   - After reaching the last character, return True only if is_end is True.

4. startsWith(prefix)
   - Start from the root.
   - Traverse each character in the prefix.
   - If any character is missing, return False.
   - If all characters exist, return True.
'''