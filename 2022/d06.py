import os

def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data

def findFirst(txt, n):
    for i in range(len(txt)-n):
        if len(set(txt[i:i+n])) == n:
            return i + n

def main():
    txt = loadData('.in')

    print("\nPart 1")
    print(findFirst(txt, 4))

    print("\nPart 2")
    print(findFirst(txt, 14))


    pass


if __name__ == "__main__":
    main()
