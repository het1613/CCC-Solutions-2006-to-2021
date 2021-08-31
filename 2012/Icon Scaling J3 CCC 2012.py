k=int(input('Enter k: '))

def line1(k):
    output='*'*k+'x'*k+'*'*k
    return output

def line2(k):
    output=' '*k+'x'*k+'x'*k
    return output

def line3(k):
    output='*'*k+' '*k+'*'*k
    return output

for i in range(k):
    print(line1(k))
    
for i in range(k):
    print(line2(k))
    
for i in range(k):
    print(line3(k))
    
