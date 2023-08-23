class Trie:

    def __init__(self):
        self.root = {}        

    def insert(self, word: str) -> None:
        cur_ent = self.root
        for ltr in word:
            if ltr not in cur_ent:
                cur_ent[ltr] = {}
            cur_ent = cur_ent[ltr]
        cur_ent['*'] = ''

    def search(self, word: str) -> bool:
        cur_ent = self.root
        for ltr in word:
            if ltr not in cur_ent:
                return False
            cur_ent = cur_ent[ltr]
        return '*' in cur_ent

    def startsWith(self, prefix: str) -> bool:
        cur_ent = self.root
        for ltr in prefix:
            if ltr not in cur_ent:
                return False
            cur_ent = cur_ent[ltr]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)