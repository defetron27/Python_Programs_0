x = [3,1,2,3]

for i in range(len(x)):
    for j in range(len(x)):
        if x[i] < x[j]:
            temp = x[j]
            x[j] = x[i]
            x[i] = temp

print(x)

max = x[len(x)-1]

print(max)

count = 0

for i in x:
    if i == max:
        count += 1

print(count)
