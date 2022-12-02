print((lambda a,b:a*2-3*b)(11,3))

x = lambda a,b,c=2:(a+b)*c
print(x(3,2,7))
print(x(3,2))

def lam(a,b,c=2):
    return (a+b)*c

print(lam(3,3,3))
print(lam(3,2))

def multi(n):
    return lambda a:a*n

d = multi(56)
print(d(6))
print(multi(4)(3))

nb = [3,6,0,-2,16,17,23,24,90,99,101,120,-9,0,12,8]
