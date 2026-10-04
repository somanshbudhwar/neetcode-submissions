class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        curr=self.root
        for w in word:
            if w not in curr.children:
                curr.children[w]=TrieNode()
            curr=curr.children[w]
        curr.endOfWord=True
        

    def search(self, word: str) -> bool:
        def dfs(curr,i):
            for j in range(i,len(word)):
                if word[j]=='.':
                    for child in curr.children:
                        if dfs(curr.children[child],j+1):
                            return True
                    return False
                else:
                    if word[j] in curr.children:
                        curr=curr.children[word[j]]
                    else:
                        return False
            return curr.endOfWord

        res = dfs(self.root,0)
        print(res)
        return res

