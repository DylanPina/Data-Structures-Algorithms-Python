class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()        

        def dfs(row: int, col: int, node: Optional[TrieNode], word: str) -> None:
            if (row < 0 or col < 0 or row == ROWS or col == COLS
                or (row, col) in visit or board[row][col] not in node.children):
                return

            visit.add((row,col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isWord:
                res.add(word)
            
            dfs(row - 1, col, node, word)
            dfs(row + 1, col, node, word)
            dfs(row, col - 1, node, word)
            dfs(row, col + 1, node, word)
            visit.remove((row, col))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")
        
        return list(res)