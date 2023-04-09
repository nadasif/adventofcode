import re

from lib.mylib import loadData


class Bag:
    bags = dict()

    def __init__(self, name):
        self.__name = name
        self.__bags = dict()

    def __repr__(self):
        if self.__bags.items():
            named = {b.__name: q for b, q in self.__bags.items()}
            return f'<Bag {self.__name} has {named}>'
        else:
            return f'<Bag {self.__name} ({len(self.__bags)})>'

    def __hash__(self):
        return hash(self.__name)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def add(self, bag, qty):
        self.__bags[bag] = qty

    def has(self, bag):
        if self.__bags:
            return bag in self.__bags or any(map(lambda b: b.has(bag), self.__bags.keys()))
        return False

    def contents_count(self, n):
        if self.__bags:
            return sum(map(lambda t: n * t[1] + t[0].contents_count(n * t[1]), self.__bags.items()))
        return 0

    @classmethod
    def parse(cls, txt):
        name, contents = txt.split(' bags contain ')
        cls.bags[name] = cls.bags.get(name) or cls(name)
        for bag in contents.strip('.').split(','):
            str_qty, name2 = list(filter(None, re.split(r'([0-9]) (.+) bags?', bag.strip())))
            cls.bags[name2] = cls.bags.get(name2) or cls(name2)
            cls.bags[name].add(cls.bags[name2], int(str_qty))


def main():
    lines = loadData().split('\n')
    list(map(Bag.parse, filter(lambda s: s.count('contain no other') == 0, lines)))
    print("\nPart 1")
    shiny = Bag.bags['shiny gold']
    print(len(list(filter(lambda b: b.has(shiny), Bag.bags.values()))))

    print("\nPart 2")
    print(shiny.contents_count(1))


if __name__ == "__main__":
    main()
