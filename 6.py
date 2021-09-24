from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    lst = [1, 2, 2, 3, 4, 5, 4]
    print([x for x,c in OrderedCounter(lst).items() if c==1])
