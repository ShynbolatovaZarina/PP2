def do_squares(N):
    for i in range(1, N+1):
        yield i**2

N = 5
for square in do_squares(N):
    print(square)


def even(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input())
for num in even(n):
    print(num, end=",")


def div34(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for x in div34(n):
    print(x)


def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for x in countdown(n):
    print(x)




