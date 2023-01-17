import os

class Statement:
    def __init__(self, prog, ip):
        self._prog = prog
        self._type = prog.getAddress(ip)
        self._args = []
        if self._type in [1,2]:
            self.nextIp = ip + 4
            self._args = [prog.getAddress(ip + i + 1) for i in range(3)]
        else:
            self.nextIp = ip + 1

    def execute(self):
        self.show()
        if self._type in [1,2]:
            self.calculate()
        elif self._type == 99:
            return 0
        return 1

    def show(self):
        # print(f'{self._type}: {self._args}')
        pass

    def calculate(self):
        v1 = self._prog.getAddress(self._args[0])
        v2 = self._prog.getAddress(self._args[1])
        if self._type == 1:
            self._prog.setAddress(self._args[2], v1 + v2)
        else:
            self._prog.setAddress(self._args[2], v1 * v2)

class Program:
    def __init__(self, text):
        self._memory = [*map(int, text.split(","))]
        self._ip = 0

    def execute(self):
        stmt = self._next()
        while stmt.execute():
            stmt = self._next()

    def _next(self):
        stmt = Statement(self, self._ip)
        self._ip = stmt.nextIp
        return stmt

    def setAddress(self, loc, value):
        self._memory[loc] = value

    def getAddress(self, loc):
        return self._memory[loc]

def loadData():
    with open(f"in-{os.path.splitext(os.path.basename(__file__))[0]}.txt", "r") as f:
        return f.read().strip()

def run(text, x, y):
    prog = Program(text)
    prog.setAddress(1, x)
    prog.setAddress(2, y)
    prog.execute()
    return prog.getAddress(0)

def find(text):
    for x in range(99):
        for y in range(99):
            result = run(text, x, y)
            #print(f'{x}, {y}: {result}')
            if result == 19690720:
                return [x,y]

def main():
    text = loadData()

    print("\nPart 1")
    print(run(text, 12, 2))

    print("\nPart 2")
    pair = find(text)
    print(pair[0] * 100 + pair[1])


if __name__ == "__main__":
    main()
