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
            if '.' in cur.children:
                cur = cur.children['.']
                continue 
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            cur = node
            for i in range(len(word)):
                if word[i] == '.':
                    contain = False
                    if i == len(word) - 1:
                        for c in cur.children:
                            contain = contain or cur.children[c].end
                        return contain

                    contain = False
                    for c in cur.children:
                        contain = contain or dfs(cur.children[c], word[i+1:])
                        return contain

                elif word[i] not in cur.children:
                    return False
                
                cur = cur.children[word[i]]
            return cur.end
        
        return dfs(self.root, word)
                


        
