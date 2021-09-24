a = [5,6,7]
b = [3,6,10]

a_count = 0
b_count = 0

for i,j in zip(a,b):
    if i > j:
        a_count += 1
    elif i < j:
        b_count += 1

print(f"{a_count} {b_count}")
