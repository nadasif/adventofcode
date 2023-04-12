from functools import reduce

from lib.mylib import loadData, Stream


def main():
    groups = loadData().split('\n\n')
    print("\nPart 1")
    print(Stream(groups)
          .map(lambda s: len(set(s.replace('\n', ''))))
          .sum())

    print("\nPart 2")
    print(Stream(groups)
          .map(lambda grp: reduce(lambda s1, s2: set(s1) & set(s2), grp.split('\n')))
          .map(len).sum())


if __name__ == "__main__":
    main()
