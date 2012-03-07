#Write a program that will find the initial number
#of coconuts.


def f(n):
    return (n - 1) / 5.0 * 4


def f6(n):
    for i in range(6):
        n = f(n)
    return n


def is_int(n):
    return abs(n - int(n)) < 0.0000001

# Enter code here.

#15621
i = 0
while True:
    i = i + 1
    r = f6(i)
    if (is_int(r)):
        print i
        break
