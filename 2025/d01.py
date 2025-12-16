from lib.mylib import loadDataNew, Counter

class Dial:
    def __init__(self, start=0, end=99, current=50):
        self.start = start
        self.end = end
        self.current = current
        self.size = end - start + 1
        self.triggers = {}

    def addTrigger(self, position, callback):
        self.triggers[position % self.size] = callback

    def set(self, position):
        self.current = position % self.size

    def move(self, instruction):
        direction = instruction[0]
        n = int(instruction[1:])
        if direction == 'L':
            self.__move(-n)
        elif direction == 'R':
            self.__move(n)

    def __move(self, n):
        while abs(n) >= self.size:
            if n > 0:
                n -= self.size
            else:
                n += self.size
            
            # Trigger all positions
            for pos, callback in self.triggers.items():
                callback()  

        for _ in range(abs(n)):
            if n > 0:
                self.__inc()
            else:
                self.__dec()
    
    def __inc(self):
        self.current += 1
        if self.current > self.end:
            self.current = self.start
        self.__calback()


    def __dec(self):
        self.current -= 1
        if self.current < self.start:
            self.current = self.end
        self.__calback()

    def __calback(self):
        # Check for triggers
        if self.current in self.triggers:
            self.triggers[self.current]()



def main():
    txt = loadDataNew()

    print("\nPart 1")
    counter = Counter()
    dial = Dial()
    for line in txt.splitlines():
        dial.move(line)
        if dial.current == 0:
            counter.inc()
    print(counter.count)
    
    print("\nPart 2")
    dial.current = 50
    counter = Counter()
    dial.addTrigger(0, counter.inc)
    for line in txt.splitlines():
        dial.move(line)
    print(counter.count)

main()