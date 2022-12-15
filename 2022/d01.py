import os

def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data



def main():
    txt = loadData('.in')
    elvesCal = txt.split('\n\n')

    lst = list(map(lambda ec : sum(map(int, ec.split())) , elvesCal))
    print("\nPart 1")
    print( max(lst))
    print("\nPart 2")
    print(sum(sorted(lst, reverse=True)[0:3]))

    pass


if __name__ == "__main__":
    main()
