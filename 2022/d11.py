import os
import math

def log(s):
    #print(s)
    pass

relief = lambda n:  math.floor(n / 3.0)

class Monkey:
    def __init__(self, txt):
        lines = txt.split('\n')
        self.id = lines[0][7]
        self.items = list(map(int, lines[1][18:].split(', ')))
        self.op = lines[2][23]
        self.num = lines[2].split(self.op + ' ')[1]
        if self.num != 'old':
            self.num = int(self.num)
        self.divBy = int(lines[3][21:])
        self.thenM = int(lines[4][29])
        self.elseM = int(lines[5][30])
        self.inspectCount = 0

    def levelOp(self, old, others):
        num = old if isinstance(self.num, str) else self.num
        new = old * num if self.op == '*' else old + num
        log(f'   new worry level: {old} {self.op} {num} : {new}')

        new = relief(new)
        log(f'   bored, new level: div by 3: {new}')

        test: bool = (new % self.divBy) == 0
        log(f'   is div by {self.divBy}? {test}')
        to = self.thenM if test else self.elseM
        log(f'   throw {new} to monkey {to}')
        others[to].throwTo(new)

    def throwTo(self, item):
        self.items.append(item)

    def inspect(self, others):
        log(f'Monkey {self.id}:')

        while len(self.items) > 0:
            item = self.items.pop(0)
            log(f'  item with worry level: {item}')
            self.levelOp(item, others)
            self.inspectCount += 1



    def __repr__(self):
        return f"\n\nMonkey {self.id}:\n  From: {self.items}\n  Op: new = old {self.op} {self.num}\n  if div by {self.divBy} then to {self.thenM} else to {self.elseM}"

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
    global relief

    txt = loadData('.in')
    monkeys = list(map(Monkey, txt.split('\n\n')))
    # print(monkeys)

    print("\nPart 1")
    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect(monkeys)

    counts = sorted([m.inspectCount for m in monkeys], reverse=True)
    print(counts[0] * counts[1])

    relief = lambda n: n % 9699690

    print("\nPart 2")
    monkeys = list(map(Monkey, txt.split('\n\n')))
    for i in range(10000):
        for monkey in monkeys:
            monkey.inspect(monkeys)
    counts = sorted([m.inspectCount for m in monkeys], reverse=True)
    print(counts[0] * counts[1])


    pass


if __name__ == "__main__":
    main()
