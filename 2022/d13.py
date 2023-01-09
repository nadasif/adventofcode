import os
from functools import cmp_to_key


def comp(lt, rt):
    # print(f' - Compare {lt} vs {rt}')

    if isinstance(lt, int) and isinstance(rt, int):
        return 0 if lt == rt else -1 if lt < rt else 1
    elif isinstance(lt, list) and isinstance(rt, int):
        return comp(lt, [rt])
    elif isinstance(lt, int) and isinstance(rt, list):
        return comp([lt], rt)

    i = 0
    while i < len(lt) and i < len(rt):
        c = comp(lt[i], rt[i])
        if c != 0:
            return c
        i += 1
    if i == len(lt) and i < len(rt):
        return -1
    elif i == len(rt) and i < len(lt):
        return 1
    else:
        return 0


def loadData(ext: str):
    filename = os.path.splitext(__file__)[0] + ext
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data


def main():
    txt = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''
    txt = loadData('.in')
    lines = txt.split('\n\n')
    s = 0
    for n in range(len(lines)):
        a, b = map(eval, lines[n].split("\n"))
        # print()
        if comp(a, b) == -1:
            # print("Good")
            s += (n + 1)

    print("Part 1")
    print(s)

    lines = list(map(eval, txt.split()))
    lines.append([[2]])
    lines.append([[6]])
    lines = sorted(lines, key=cmp_to_key(comp))

    for i, lst in enumerate(lines):
        #print(f"{i}: {lst}")
        if lst == [[2]]:
            a = i + 1
        elif lst == [[6]]:
            b = i + 1

    print("Part 2")
    print(a * b)


if __name__ == "__main__":
    main()
