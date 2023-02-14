from lib.mylib import loadData


def zero(floor, n):
    floor[0] += n
    return floor[0] == -1


def main():
    txt = loadData()
    lst = [1 if c == '(' else -1 for c in txt]

    print("\nPart 1")
    print(sum(lst))

    print("\nPart 2")
    floor = [0]
    print(1 + next(filter(lambda i: zero(floor, lst[i]), range(len(lst)))))


if __name__ == "__main__":
    main()
