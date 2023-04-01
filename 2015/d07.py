import enum

from lib.mylib import loadData

Wire = None


def num_or_var(val: any) -> any:
    return None if val is None else int(val) if val.isdigit() else val


def eval(val: any) -> int:
    if isinstance(val, int):
        return val
    elif Wire is not None:
        return Wire.byName[val].get_value()
    else:
        raise TypeError()


class Gate(enum.Enum):
    VALUE = enum.auto()
    LSHIFT = enum.auto()
    RSHIFT = enum.auto()
    AND = enum.auto()
    OR = enum.auto()
    NOT = enum.auto()


class Expr:
    def __init__(self, txt):
        parts = txt.split()
        size = len(parts)
        self.value2 = None
        if size == 1:
            self.gate = Gate.VALUE
            self.value = num_or_var(parts[0])
        elif size == 2:
            self.gate = Gate.NOT
            self.value = num_or_var(parts[1])
        else:
            self.gate = Gate[parts[1]]
            self.value = num_or_var(parts[0])
            self.value2 = num_or_var(parts[2])

    def __solve_not(self):
        return (~ eval(self.value)) & 0xFFFF

    def __solve_binary(self):
        if self.gate == Gate.OR:
            return eval(self.value) | eval(self.value2)
        elif self.gate == Gate.AND:
            return eval(self.value) & eval(self.value2)
        elif self.gate == Gate.RSHIFT:
            return eval(self.value) >> eval(self.value2)
        else:
            return 0xFFFF & (eval(self.value) << eval(self.value2))

    def set_value(self, value):
        self.gate = Gate.VALUE
        self.value = value

    def get_value(self):
        if self.gate is Gate.NOT:
            return self.__solve_not()
        elif self.gate is not Gate.VALUE:
            return self.__solve_binary()
        return eval(self.value)

    def __repr__(self):
        return f"<Expr {self.gate.name}({self.value}, {self.value2})>"


class Wire:
    byName = dict()

    def __init__(self, expr):
        parts = expr.split(' -> ')
        self.name = parts[1]
        self.value = None
        self.expr = Expr(parts[0])
        Wire.byName[self.name] = self

    @staticmethod
    def reset():
        for wire in Wire.byName.values():
            wire.value = None

    def set_value(self, value):
        self.expr.set_value(value)

    def get_value(self):
        if self.value is None:
            self.value = self.expr.get_value()
        return self.value

    def __repr__(self):
        return f"<Wire {self.name} = {self.expr}>"


def main():
    txt = loadData()
    lines = txt.split("\n")
    list(map(Wire, lines))
    print("\nPart 1")
    value_of_a = Wire.byName['a'].get_value()
    print(f"{value_of_a}")

    print("\nPart 2")
    Wire.reset()
    Wire.byName['b'].set_value(value_of_a)
    value_of_a = Wire.byName['a'].get_value()
    print(f"{value_of_a}")


if __name__ == "__main__":
    main()
