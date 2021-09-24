x = [2,4,1,3,5]

#sort

for i in range(len(x)):
    for j in range(len(x)):
        if x[j] > x[i]:
            temp = x[j]
            x[j] = x[i]
            x[i] = temp

#x.sort()
#sorted(x)

#print(x)

min = 0
max = 0

for i,j in zip(range(0,len(x)-1),range(1,len(x))):
    min += x[i]
    max += x[j]

print(min,max)
