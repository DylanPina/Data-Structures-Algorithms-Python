class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(offset: int, root: Optional[TrieNode]) -> bool:
            cur = root

            for i in range(offset, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                if c not in cur.children:
                    return False
                cur = cur.children[c]
            return cur.word
            
        return dfs(0, self.root)