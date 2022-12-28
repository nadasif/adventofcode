import os

class Command:
    def __init__(self, txt):
        self.cycles = 1 if txt == 'noop' else 2
        self.num = 0 if self.cycles == 1 else int(txt[5:])

    def add(self, n):
        return n + self.num

    def __repr__(self):
        return f"#<P1:>"


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def main():
    txt = loadData('.in')
    cmds = list(map(Command, txt.split('\n')))

    print("\nPart 1")
    cycle = 0
    x = 1
    s = 0
    for cmd in cmds:
        for c in range(cmd.cycles):
            cycle += 1
            if ((cycle + 20) % 40) == 0:
                signal = x * cycle
                s += signal
                print(signal)
        x = cmd.add(x)

    print(s)


    print("\nPart 2")
    crt = [' '] * 240
    cycle = 0
    x = 1
    for cmd in cmds:
        for c in range(cmd.cycles):
            if x <= (cycle % 40 + 1) <= (x+2):
                crt[cycle] = '#'
            cycle += 1
        x = cmd.add(x)

    print(''.join(crt[0:40]))
    print(''.join(crt[40:80]))
    print(''.join(crt[80:120]))
    print(''.join(crt[120:160]))
    print(''.join(crt[160:200]))
    print(''.join(crt[200:240]))

    pass


if __name__ == "__main__":
    main()
