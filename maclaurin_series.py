nth_term = int(input("Enter n-th term: "))
x = int(input("Enter x: "))
sum = 0

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

for k in range(0, nth_term + 1):
    sum += ( ( (-1)**k) * (x**(2*k) ) ) / fact(2*k)

print(sum)
