if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    s.__contains__()

    for i in range(N):
        lst = list(input().split())
        query = lst[0]
        if query == 'remove':
            print('remove')
            if lst[1] in s:
                s.remove(lst[1])
        if query == 'discard':
            print('discard')
            s.discard(lst[1])
        if query == 'pop':
            print('pop')
            if len(s) > 0:
                s.pop()
    print(s)

    s.symmetric_difference