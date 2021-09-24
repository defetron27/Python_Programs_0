x = [73,67,38,33]

for i in range(len(x)):
    if x[i] > 37:
        mul = 5 - (x[i]%5)
        if mul < 3:
            x[i] += mul
print(x)
            
            
            
