# stuart = 0
# kevin = 0
# words = ['apple', 'orange', 'pear', 'milk', 'otter', 'snake','iguana','tiger','eagle']
# # vowel = [[0,1][x[0] in "aeiou"] for x in words]
# vowel = list(map(lambda x: [0,1][x[0] in "aeiou"],words))
# stuart = vowel.count(1)
# kevin = vowel.count(0)

# print(stuart)
# print(kevin)

# A=[[x*100, x][x % 2 != 0] for x in range(1,11)]
# print(A)

# print (list(map(lambda x: [x*10, x][x % 2 != 0], range(1,10))))

# s = set([1,2,3,4,5,6,7,8,9])

# s.pop()

# print(s)


# if 9 in s:
#     s.remove(9)

# print(s)

a = {1,2,3,4}
b = {11,8,7,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.isdisjoint(b))