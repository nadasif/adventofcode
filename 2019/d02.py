
class Statement:
    def __init__(self, prog, ip):
        self.__prog = prog
        self.__type = prog.getAddress(ip)
        self.__args = []
        if self.__type in [1,2]:
            self.nextIp = ip + 4
            self.__args = [prog.getAddress(ip + i + 1) for i in range(3)]
        else:
            self.nextIp = ip + 1

    def execute(self):
        self.show()
        if self.__type in [1,2]:
            self.calculate()
        elif self.__type == 99:
            return 0
        return 1

    def show(self):
        # print(f'{self.__type}: {self.__args}')
        pass

    def calculate(self):
        v1 = self.__prog.getAddress(self.__args[0])
        v2 = self.__prog.getAddress(self.__args[1])
        if self.__type == 1:
            self.__prog.setAddress(self.__args[2], v1 + v2)
        else:
            self.__prog.setAddress(self.__args[2], v1 * v2)

class Program:
    def __init__(self, text):
        self.__memory = [*map( int, text.split(","))]
        self.__ip = 0

    def execute(self):
        stmt = self.__next()
        while stmt.execute():
            stmt = self.__next()

    def __next(self):
        stmt = Statement(self, self.__ip)
        self.__ip = stmt.nextIp
        return stmt

    def setAddress(self, loc, value):
        self.__memory[loc] = value

    def getAddress(self, loc):
        return self.__memory[loc]

def loadData():
    filename = __file__[:-3] + ".in"
    file1 = open(filename, 'r')
    text = file1.read()
    file1.close()
    return text

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
    print(f'Part 1: {run(text, 12, 2)}')
    pair = find(text)
    print(f'Part 2: {pair[0] * 100 + pair[1]}')

if __name__ == '__main__':
    main()

