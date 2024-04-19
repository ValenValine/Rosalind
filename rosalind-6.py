def rabbit(n,k):
    if n == 1 or n== 2:
        return 1
    else:
        return rabbit(n-1, k) + k * rabbit(n-2, k)
    
n = int(input("Enter n:"))
k = int(input("Enter k:"))
    
rabbits= str(rabbit(n,k))
print(rabbits)