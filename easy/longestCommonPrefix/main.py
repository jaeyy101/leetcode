class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)

        return trie.commonPrefix()


class TrieNode:
    def __init__(self):
        self.children = {}  # To hold children nodes
        self.is_word = False


class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str):
        node = self.head
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def commonPrefix(self):
        node = self.head

        prefix = ""
        while len(node.children) == 1 and not node.is_word:
            key = list(node.children)[0]
            prefix += key
            node = node.children[key]

        return prefix


instance = Solution()
print(instance.longestCommonPrefix(["ab", ""]))
