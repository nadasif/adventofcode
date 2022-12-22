import os

class Node:
    def __init__(self, name, size = 0):
        self.name, self.size, self.nodes, self.parent = name, size, [], None
        self.isDir = (size == 0)

    def add(self, node):
        self.nodes.append(node)
        node.parent = self

    def _level(self):
        n = 0
        node = self
        while node:
            n += 1
            node = node.parent
        return n

    def find(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
    def calcSize(self):
        s = 0
        for node in self.nodes:
            if node.isDir:
                s += node.calcSize()
            else:
                s += node.size
        self.size = s
        return self.size

    def __repr__(self):
        result = f"#<Node: {self.name} {self.size}"
        for node in self.nodes:
            result += "\n" + ("  " * node._level()) + f"{node}"
        result += ">"
        return result

def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

class Parser:
    def __init__(self, txt, root):
        self.lines = txt.split("\n")
        self.root = root
        self.pwd = root

    def parse(self):
        for line in self.lines:
            parts = line.split()
            if parts[0] == '$':
                self._parseCommand(parts)
            else:
                self._addChild(parts)

    def _parseCommand(self, parts):
        if parts[1] == 'ls':
            return
        if parts[2] == '/':
            self.pwd = self.root
        elif parts[2] == '..':
            self.pwd = self.pwd.parent
        else:
            self.pwd = self.pwd.find(parts[2])

    def _addChild(self, parts):
        if parts[0] == 'dir':
            self.pwd.add(Node(parts[1]))
        else:
            self.pwd.add(Node(parts[1], int(parts[0])))

def dirSize(lst, node: Node, fn):
    if not node.isDir:
        return
    # print(node.name)
    if fn(node.size):
        lst.append(node)
    for n in node.nodes:
        dirSize(lst, n, fn)

def main(): #268565
    txt = loadData('.in')
    root = Node('/')
    Parser( txt, root).parse()
    root.calcSize()
    #print(root)

    print("\nPart 1")
    lst = []
    dirSize(lst, root, lambda s: s<=100000)
    print(sum(map(lambda n: n.size, lst)))

    print("\nPart 2")
    lst = []
    dirSize(lst, root, lambda s: s>=268565)
    print(min(map(lambda n: n.size, lst)))


if __name__ == "__main__":
    main()
