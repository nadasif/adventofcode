import os

class Stacks:
    def __init__(self, txt):
        lines = txt.split("\n")
        self.names = lines.pop().split()
        self.stacks = {n: [] for n in self.names}
        lines.reverse()
        for line in lines:
            i = 0
            for crate in list(map(lambda l: line[l], range(1, len(line), 4))):
                i += 1
                if crate != ' ':
                    self.stacks[str(i)].append(crate)

    def command(self, cmd):
        parts = cmd.split()
        count = int(parts[1])
        from_st = parts[3]
        to_st = parts[5]
        for i in range(count):
            self.stacks[to_st].append( self.stacks[from_st].pop())

    def command2(self, cmd):
        parts = cmd.split()
        count = int(parts[1])
        from_st = parts[3]
        to_st = parts[5]
        loc = len(self.stacks[to_st])
        for i in range(count):
            self.stacks[to_st].insert(loc, self.stacks[from_st].pop())

    def peek(self, key):
        value = self.stacks[key].pop()
        self.stacks[key].append(value)
        return value

    def tops(self):
        return ''.join(map(lambda l: self.peek(l), self.names))


    def __repr__(self):
        return f"#<P1: {self.stacks}>"

class Part2:
    def __init__(self, txt):
        pass

    def __repr__(self):
        return f"#<P2:>"


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def main():
    txt = loadData('.in')

    sections = txt.split("\n\n")
    stacks = Stacks(sections[0])

    print("\nPart 1")
    for cmd in sections[1].split("\n"):
        stacks.command(cmd)
    print(stacks.tops())

    stacks = Stacks(sections[0])
    print("\nPart 2")
    for cmd in sections[1].split("\n"):
        stacks.command2(cmd)
    print(stacks.tops())

    pass


if __name__ == "__main__":
    main()
