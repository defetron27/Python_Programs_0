if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    aSet = set(map(int,input().split()))
    bSet = set(map(int,input().split()))

    happiness = 0

    for i in aSet:
        happiness += arr.count(i)
    
    for i in bSet:
        happiness -= arr.count(i)

    print(i)