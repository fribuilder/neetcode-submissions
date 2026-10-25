class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        res = True
        def find(word, cur):
            nonlocal res
            if not word:
                return cur.end
            elif not cur:
                return False

            ch = word[0]
            if ch == '.':
                for child in cur.children.values():
                    if find(word[1:], child):
                        return True
                return False
            elif ch not in cur.children:
                return False
            else:
                return find(word[1:], cur.children[ch])
        
        return find(word, self.root)

                


        
