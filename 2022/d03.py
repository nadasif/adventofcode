import os

class Part1:

    def __init__(self, txt):
        n = int(len(txt)/2)
        s = list(set(txt[0:n]) & set(txt[n:]))
        if s[0].islower():
            self.score = ord(s[0]) - 96
        else:
            self.score = ord(s[0]) - 64 + 26

    def __repr__(self):
        return f"#<P1: {self.score}>"

class Part2:
    def __init__(self, lst):
        s = list(set(lst[0]) & set(lst[1]) & set(lst[2]))
        if s[0].islower():
            self.score = ord(s[0]) - 96
        else:
            self.score = ord(s[0]) - 64 + 26

    def __repr__(self):
        return f"#<P2: {self.score}>"


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def score(p):
    return p.score

def main():
    txt = loadData('.in')
    lines = txt.split('\n')

    print("\nPart 1")
    p1s = list(map(Part1, lines))
    print(sum(map(score,p1s)))

    print("\nPart 2")
    p2s = list(map(Part2, [lines[n:n+3] for n in range(0,len(lines), 3)]))
    print(sum(map(score,p2s)))


    pass


if __name__ == "__main__":
    main()
