def dups(n: int) -> dict:
    grp = dict()
    ds = [int(x) for x in str(n)]
    for i in range(1,6):
        d = ds[i]
        if d < ds[i-1]:
            return dict() # empty dictionary means failed
        elif d == ds[i-1]:
            grp[d] = grp.get(d,1) + 1
    return grp


def main():
    count1 = 0
    count2 = 0
    for n in range(246515, 739106+1):
        grp = dups(n)
        if grp:
            count1 += 1
        if any(v == 2 for v in grp.values()):
            count2 += 1
    print(f'{count1}, {count2}')

if __name__ == '__main__':
    main()
