# x = [11,21,21,32,32,51,62,26,64]

# y = list(set(x))

# for i in set(x):
#     print(i,x.count(i))

x = [2,1,4,3]

x.sort()

print(x)

if __name__ == '__main__':
    n = int(input())
    x = list(map(int,input().split()))

    mean = 0.0

    for i in x:
        mean = mean + i

    mean = mean/len(x)

    x.sort()

    if len(x)%2 == 0:
        median = x[len(x[:len(x)-1])//2] + x[len(x)//2]

    mode = 0
    modeCount = dict()
    y = set(x)

    for i in y:
        modeCount[i] = x.count(i)

    print(mode)

