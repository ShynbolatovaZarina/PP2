import math

l = [2, 3, 4, 5]
p = math.prod(l)
print(p)

l = [2, 3, 4, 5]
p= 1
for number in l:
    p *= number
print(p)


def f(s):
    u = 0
    l = 0
    for i in s:
        if i.isupper():
            u += 1
        elif i.islower():
            l += 1
    return u, l

a, b = f()

print(a)
print(b)

def bts(a):
    text=a.lower()
    polidrome=text[::-1]
    if a==polidrome:
        return True
    else:
        return False
a=str(input())


from time import sleep
import math

def root(n):
    
    return pow(n, 0.5)

ms=float(input())
n=int(input)
sleep(ms/1000)
root()

t = tuple(input().split())
print(all(t))


