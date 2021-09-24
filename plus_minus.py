import re

x = [-1,-3,0,5,6,7]

p_count = 0
n_count = 0
z_count = 0

for i in x:
    if i == 0:
        z_count += 1
    else:
        search = re.search(r'(-.*)',str(i),re.M|re.I)
        if search:
            n_count += 1
        else:
            p_count += 1

print(p_count,n_count,z_count)

print("%.6f"%(p_count / len(x)),"%.6f"%(n_count / len(x)),"%.6f"%(z_count / len(x)),sep="\n")
