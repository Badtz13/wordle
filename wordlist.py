class Wordlist:
    def __init__(self) -> None:
        self.root: WordlistNode = WordlistNode()

    def addString(self, string) -> None:
        traversalNode = self.root
        for char in string:
            tempNode = traversalNode.children.get(char)
            if tempNode == None:
                tempNode = WordlistNode()
                traversalNode.addChild(char, tempNode)
            traversalNode = tempNode
        traversalNode.endOfString = True

    def removeCharPos(self, char, pos) -> None:
        self.root.removeCharPos(char, pos)

#    def exclusiveCharPos(self, char, pos) -> None:
#        self.root.exclusiveCharPos(char, pos)

    def printTrie(self) -> None:
        self.root.printTrie()
        print()

    def numWords(self) -> int:
        return self.root.count()

class WordlistNode:
    def __init__(self) -> None:
        self.children: Dict[str, WordlistNode] = {}
        self.endOfString: bool = None

    def addChild(self, char, node) -> None:
        self.endOfString = False
        self.children.update({char:node})

    def removeCharPos(self, char, pos) -> None:
        if pos == 0:
            if char in self.children:
                self.children.pop(char)
            return
        if self.endOfString:
            return

        for _, child in self.children.items():
            child.removeCharPos(char, pos-1)

    def printTrie(self) -> None:
        for char, child in self.children.items():
            if child.endOfString:
                print(f"{char} ", end="")
            else:
                print(f"{char}:(", end="")
                child.printTrie()
                print(") ", end="")

    def count(self) -> int:
        ends = 0
        for _, child in self.children.items():
            if child.endOfString:
                ends += 1
            else:
                ends += child.count()
        return ends

if __name__ == "__main__":
    words = [word.rstrip() for word in open('validAnswers.txt').readlines()]
    #words = ["cigar", "civil", "civic", "arose", "soare", "sorts"]
    newTrie = Wordlist()
    for word in words:
        newTrie.addString(word)
    print(newTrie.numWords())
    newTrie.removeCharPos("v", 2)
    print(newTrie.numWords())
