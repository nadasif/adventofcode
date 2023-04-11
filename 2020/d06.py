from functools import reduce

from lib.mylib import loadData


def main():
    groups = loadData().split('\n\n')
    print(groups)
    print("\nPart 1")
    print(sum(map(lambda s: len(set(s.replace('\n', ''))), groups)))

    print("\nPart 2")
    print(sum(map(len, map(lambda group: reduce(lambda s1, s2: set(s1) & set(s2), group.split('\n')), groups))))


if __name__ == "__main__":
    main()
