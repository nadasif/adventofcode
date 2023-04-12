from lib.mylib import loadData

class Register:
    def __init__(self):
        self.__value = 0
        self.__ip = 0

    def add(self, value):
        self.__value += value

    def addIp(self, value):
        self.__ip += value

    def value(self):
        return self.__value

    def ip(self) -> int:
        return self.__ip

    def __repr__(self):
        return f'<Register acc:{self.__value}, ip:{self.__ip}>'


class Op:
    def __init__(self, txt):
        self.__op, n = txt.split()
        self.__val = int(n)

    def __repr__(self):
        return f'<Op {self.__op} {self.__val}>'

    def execute(self, register: Register):
        if self.__op == 'jmp':
            register.addIp(self.__val)
        elif self.__op == 'acc':
            register.add(self.__val)
            register.addIp(1)
        else:
            register.addIp(1)

    def toggle(self):
        self.__op = 'jmp' if self.__op == 'nop' else 'nop'

    def not_acc(self) -> bool:
        return self.__op != 'acc'


def execute(ops) -> Register:
    reg = Register()
    ips = set()
    while reg.ip() not in ips:
        ips.add(reg.ip())
        if reg.ip() > len(ops):
            reg.addIp(-1000)
            break
        elif reg.ip() == len(ops):
            break
        ops[reg.ip()].execute(reg)
    return reg


def main():
    ops = list(map(Op, loadData().split('\n')))

    print("\nPart 1")
    reg = execute(ops)
    print(reg.value())

    print("\nPart 2")
    ops_not_acc = filter(Op.not_acc, ops)
    op = next(ops_not_acc)
    op.toggle()
    reg = execute(ops)
    while reg.ip() < len(ops):
        op.toggle()
        op = next(ops_not_acc)
        op.toggle()
        reg = execute(ops)
    print(reg.value())


if __name__ == "__main__":
    main()
