class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur["end"] = True

    def search(self, word: str) -> bool:
        def dfs(i,cur):
            if i == len(word):
                return "end" in cur
            
            if word[i] != ".":
                if word[i] not in cur:
                    return False
                return dfs(i+1,cur[word[i]])
            
            if word[i] == ".":
                for k, c in cur.items():
                    if k == "end":
                        continue
                    
                    if dfs(i+1,c):
                        return True
                return False

        return dfs(0,self.root)