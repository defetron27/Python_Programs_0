x1 = 0
v1 = 3
x2 = 4
v2 = 2

print(x1,v1,x2,v2)
for i,j in zip(range(x1,10001,v1),range(x2,10001,v2)):
    if i == j:
        print(i,j)
        print("YES")
        break;
for i in range(x1+v1+x2+v2):
    
    if x1 + v1 * i == x2 + v2 * i:
        print("Yes")
        print(x1+v1+x2+v2)
        break
    #else:
        #print(x1 + v1 * i, x2 + v2 * i)
if((x2+x1)%(v2+v1) == 0):
    print("YES")
else:
    print("NO")
