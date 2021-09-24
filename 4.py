from collections import OrderedDict

if __name__ == '__main__':
    # n = int(input())
    a = {2,3,5,9}
    # m = int(input())
    b = {2,3,11,12}

    aDb = a.difference(b)
    bDa = b.difference(a)

    aUb = sorted(aDb.union(bDa))
    
    for i in aUb:
        print(i)