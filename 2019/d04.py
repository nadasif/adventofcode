def none_dec(ds):
    return all(ds[i]<=ds[i+1] for i in range(5))

def has_pair(ds):
    return any(ds[i]==ds[i+1] for i in range(5))

def exact_pair(ds):
    d = dict()
    for i in ds:
        d[i] = d.get(i,0) + 1
    return any(n==2 for n in d.values())

def main():
    count = 0
    for n in range(246515, 739106+1):
        ds = [int(x) for x in str(n)]
        if none_dec(ds) and has_pair(ds) and exact_pair(ds):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
