def evens(N):
    
    for x in range(1, N + 1):
        if(x % 2 == 0):
            yield x
    
    
N = int(input())

evens = evens(N)

for even in evens:
    print(even)