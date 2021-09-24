s = 7
t = 10
a = 4
b = 12
m = [2,3,-4]
n = [3,-2,-4]

m_count = 0
n_count = 0

for i in m:
    p = a + i
    if p >= s and p <= t:
        m_count += 1
        
for i in n:
    p = b + i
    print(p)
    if p >= s and p <= t:      
        n_count += 1

print(m_count,n_count)
