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

    def printTrie(self) -> None:
        self.root.printTrie()

class WordlistNode:
    def __init__(self) -> None:
        self.children: Dict[str, WordlistNode] = {}
        self.endOfString: bool = None

    def addChild(self, char, node) -> None:
        self.endOfString = False
        self.children.update({char:node})

    def printTrie(self) -> None:
        for char, child in self.children.items():
            if child.endOfString:
                print(f"{char} ", end="")
            else:
                print(f"{char}:(", end="")
                child.printTrie()
                print(") ", end="")

if __name__ == "__main__":
    #words = [word.rstrip() for word in open('validAnswers.txt').readlines()]
    words = ["cigar", "civil", "civic", "arose", "soare", "sorts"]
    newTrie = Wordlist()
    for word in words:
        newTrie.addString(word)
