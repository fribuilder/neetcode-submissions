class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                new = TrieNode()
                cur.children[ch] = new
                cur = new
            else:
                cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        return cur.end


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            else:
                cur = cur.children[ch]
        return True

        