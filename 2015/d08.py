from lib.mylib import loadData


def len0(line: str) -> int:
    return len(eval(line))


def len1(line: str) -> int:
    return len(line)


def len2(line: str) -> int:
    return len(line) + line.count('\\') + line.count('"') + 2


def main():
    lines = loadData().split("\n")

    chr_count = sum(map(len1, lines))
    mem_count = sum(map(len0, lines))

    print("\nPart 1")
    print(chr_count - mem_count)

    print("\nPart 2")
    print(sum(map(len2, lines)) - chr_count)


if __name__ == "__main__":
    main()
