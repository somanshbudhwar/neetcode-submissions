class WordDictionary:

    def __init__(self):
        self.map = {}
        

    def addWord(self, word: str) -> None:
        point = self.map
        for w in word:
            if w in point:
                point=point[w]
            else:
                point[w]={}
                point=point[w]
        point["#"]=True

        

    def search(self, word: str) -> bool:
        def search_hash(dictionary, word):
            if word=="#":
                return "#" in dictionary
            if word[0]==".":
                for key in dictionary:
                    if key=="#":
                        continue
                    if search_hash(dictionary[key],word[1:]):
                        return True
                return False
            if word[0] in dictionary:
                return search_hash(dictionary[word[0]], word[1:])
            else:
                return False     
        return search_hash(self.map, word+"#")     
        
        
