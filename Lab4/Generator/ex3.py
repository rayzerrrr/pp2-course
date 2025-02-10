def div(N):
    
    for x in range(1, N + 1):
        if(x % 3 == 0 and x % 4 == 0):
            yield x
    
    
N = int(input())

nums = div(N)

for x in nums:
    print(x)