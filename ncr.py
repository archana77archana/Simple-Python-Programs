import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

n = int(input("Input n: "))
r = int(input("Input r: "))

print("nCr: ")
print(nCr(n, r))
