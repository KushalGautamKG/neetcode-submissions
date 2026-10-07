class TrieNode:

    def __init__(self):

        self.children = {}

        self.endOfWord = False


    def addWord(self, word):

        cur = self


        for c in word:


            if c not in cur.children:
                cur.children[c] = TrieNode()


            cur = cur.children[c]

        cur.endOfWord = True





class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        self.root = TrieNode()
        for w in words:
            self.root.addWord(w)

        res = []
        
        visit = set()
        def dfs(r, c, node, word):


            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or board[r][c] not in node.children:
                return


            visit.add((r, c))

            word += board[r][c]

            node = node.children[board[r][c]]


            if node.endOfWord:
                res.append(word)
                node.endOfWord = False

            dfs(r + 1, c, node, word)

            dfs(r - 1, c, node, word)


            dfs(r, c + 1, node, word)

            dfs(r, c - 1, node, word)
            visit.remove((r, c))


        for r in range(ROWS):

            for c in range(COLS):
                dfs(r, c, self.root, "")

        return res



            



            
