ar = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

ltr = 0
rtl = 0

ar_len = len(ar)

i = 0
for j,k in zip(range(0,ar_len),range(ar_len-1,-1,-1)):
   ltr += ar[i][j]
   rtl += ar[i][k]
   i+=1

print(ltr,rtl)
