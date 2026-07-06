
class TrieNode:

    def __init__(self):
        self.children = {}


        self.endOfWord = False




class PrefixTree:

    def __init__(self):
        
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()


            cur = cur.children[w]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w not in cur.children:
                return False

            cur = cur.children[w]


        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        
        cur = self.root

        for w in prefix:
            if w not in cur.children:
                return False

            cur = cur.children[w]


        return True